from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_limit = models.DurationField()
    teacher = models.ForeignKey(User, related_name='quizzes', on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='quizzes_assigned')

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=50, choices=[('multiple_choice', 'Multiple Choice')])

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class StudentQuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='submissions', on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE)
    submission_time = models.DateTimeField(auto_now_add=True)
    score = models.FloatField()

class Answer(models.Model):
    submission = models.ForeignKey(StudentQuizSubmission, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, null=True, blank=True, on_delete=models.SET_NULL)