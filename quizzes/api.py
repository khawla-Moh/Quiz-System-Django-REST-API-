from rest_framework import viewsets,permissions
from .models import Question,Quiz,Choice,StudentQuizSubmission,Answer
from .serializers import QuizSrializers,QuestionSrializers,ChoiceSrializers,StudentQuizSubmissionSrializers,AnswerSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication



class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSrializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'Teacher':
            return Quiz.objects.filter(teacher=user)
        if user.role == 'Student':
            return Quiz.objects.filter(students=user)
        return Quiz.objects.none()
