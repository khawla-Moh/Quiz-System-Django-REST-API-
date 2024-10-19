from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_limit = models.DurationField()
    teacher = models.ForeignKey(User, related_name='quizzes_teacher', on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='quizzes_student')

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions_quiz', on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=50, choices=[('multiple_choice', 'Multiple Choice')])

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices_questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class StudentQuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='Student_Submission', on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='Student_Submission', on_delete=models.CASCADE)
    submission_time = models.DateTimeField(auto_now_add=True)
    score = models.FloatField()

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}"

class Answer(models.Model):
    submission = models.ForeignKey(StudentQuizSubmission, related_name='answers_submission', on_delete=models.CASCADE)
    question = models.ForeignKey(Question,related_name='Answer_Question' ,on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, null=True, blank=True, on_delete=models.SET_NULL)



