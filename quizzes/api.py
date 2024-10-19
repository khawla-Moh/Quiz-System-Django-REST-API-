from rest_framework import viewsets,permissions,generics
from .models import Question,Quiz,Choice,StudentQuizSubmission,Answer
from django.db import transaction,IntegrityError
from .serializers import QuizSrializers,QuestionSrializers,ChoiceSrializers,StudentQuizSubmissionSrializers,AnswerSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated





class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSrializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        # Debugging line to check user ID and role
        print(f"User ID: {user.id}, Role: {user.userprofile.role}")

        if user.userprofile.role == 'teacher':
            return Quiz.objects.filter(teacher=user)
        elif user.userprofile.role == 'student':
            quizzes = Quiz.objects.filter(students=user)
            # Debugging line to see quizzes for the student
            print(f"Quizzes for Student ID {user.id}: {list(quizzes)}")
            return quizzes
            print(quizzes)
            print(user)
            print(user)
        return Quiz.objects.none()

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSrializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class StudentQuizSubmissionViewSet(viewsets.ModelViewSet):
    queryset = StudentQuizSubmission.objects.all()
    serializer_class = StudentQuizSubmissionSrializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def create(self, request, *args, **kwargs):
        data = request.data
        
        # Fetch the quiz
        quiz = self.get_quiz(data['quiz'])
        if not quiz:
            return Response({'error': 'Quiz not found.'}, status=404)

        student = request.user
        print(f"Request data: {data}")  # Debugging line
        print(f"Request data: {student}")  # Debugging line
    # Use a transaction to ensure atomicity
        try:
          
          with transaction.atomic():
                # Debugging: Check student and quiz
                print(f"Creating submission for student: {student.id}, quiz: {quiz.id}")

                # Create submission instance
                submission = StudentQuizSubmission(quiz=quiz, student=student, score=0)
                submission.save()  # Save to generate primary key

                # Calculate score and prepare answers
                score, answers_to_create = self.grade_quiz(submission, data.get('answers', []))

                # Set the score
                submission.score = score
                
                # Create all Answer instances in bulk
                if answers_to_create:
                    Answer.objects.bulk_create(answers_to_create)

                # Save the updated submission with the score
                submission.save()  # Final save to update score
 
          return Response({'score': score})

        except IntegrityError as ie:
            print(f"IntegrityError occurred: {ie}")  # Log integrity errors
            return Response({'error': 'Database integrity error.'}, status=400)
        except Exception as e:
            print(f"Error occurred: {e}")  # Log the error
            return Response({'error': 'An error occurred while processing your request.'}, status=500)


    def get_quiz(self, quiz_id):
        try:
            return Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            return None

    def grade_quiz(self, submission, answers):
        score = 0
        answers_to_create = []  # List to hold answers to be created

        for answer_data in answers:
            question_id = answer_data['question']
            choice_id = answer_data.get('choice')
            
            # Fetch the question
            question = self.get_question(question_id)
            if not question:
                continue  # Skip invalid questions
            
            # Process the answer
            if choice_id is not None:
                choice = self.get_choice(choice_id)
                if choice:
                    answers_to_create.append(Answer(submission=submission, question=question, choice=choice))
                    if choice.is_correct:
                        score += 1  # Increment score for correct answers
        
        return score, answers_to_create



    def get_question(self, question_id):
        try:
            return Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return None

    def get_choice(self, choice_id):
        try:
            return Choice.objects.get(id=choice_id)
        except Choice.DoesNotExist:
            return None