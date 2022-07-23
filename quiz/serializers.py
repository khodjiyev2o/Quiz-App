from secrets import choice
from .models import Choice,Question,Quiz,Creator,Result

from rest_framework import serializers




"""
class QuestionSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = "__all__"

    def get_question(self, obj):
        return obj.question.text

"""

"""
class QuestionSerializer(serializers.ModelSerializer):
    choice = serializers.RelatedField(source='answer',read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
"""
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('id','username')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('option','correct')

class QuestionSerializer(serializers.ModelSerializer):
    options = ChoiceSerializer(many=True, read_only=False)

    class Meta:
        model = Question
        fields = ('id','question','options')