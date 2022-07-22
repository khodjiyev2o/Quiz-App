from django.shortcuts import render
from .models import Quiz,Question,Choice
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from quiz import serializers
# Create your views here.

def index(request):
    quiz = Quiz.objects.select_related('creator').prefetch_related('question')
    return render(request,'quiz/index.html',{'quiz':quiz})



@api_view(['GET'])
def api_questions(reqest):
    qs = Question.objects.all()
    serializer = QuestionSerializer(qs,many=True)
    return Response(serializer.data)