from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import QuizViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
""" 
router.register(r'questions', QuestionViewSet)
router.register(r'submissions', StudentQuizSubmissionViewSet)
"""
urlpatterns = [
    path('', include(router.urls)),  # Include router URLs for the app



]