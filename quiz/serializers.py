from secrets import choice
from .models import Choice,Question,Quiz,Creator

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




class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=False)

    class Meta:
        model = Question
        fields = ('id','text','choices')