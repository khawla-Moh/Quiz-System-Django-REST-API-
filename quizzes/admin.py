from django.contrib import admin
from .models  import Quiz,Question,Choice,StudentQuizSubmission,Answer,UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(StudentQuizSubmission)
admin.site.register(Answer)