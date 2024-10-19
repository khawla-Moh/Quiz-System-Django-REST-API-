from rest_framework import serializers
from .models import Question,Quiz,Choice,StudentQuizSubmission,Answer




class QuizSrializers(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields = '__all__'




class QuestionSrializers(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields = '__all__'        



class ChoiceSrializers(serializers.ModelSerializer):
    class Meta:
        model=Choice
        fields = '__all__'                


class StudentQuizSubmissionSrializers(serializers.ModelSerializer):
    class Meta:
        model=StudentQuizSubmission
        fields = '__all__'         
    
                       
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields = '__all__'         

        