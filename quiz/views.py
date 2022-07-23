from urllib import response
from django.db import IntegrityError
from django.shortcuts import render,redirect
from .models import Quiz,Question,Choice,Creator
from .serializers import QuestionSerializer,CreatorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from quiz import serializers
from rest_framework import generics

# Create your views here.

def index(request,username):
    creator = Creator.objects.filter(username=username).first()
    quiz = Quiz.objects.filter(creator=creator).select_related('creator').prefetch_related('question')
    return render(request,'quiz/index.html',{'quiz':quiz,'username':username})

def names(request):
    return render(request,'quiz/names.html',{})

@api_view(['GET'])
def api_questions(reqest):
    qs = Question.objects.all()
    serializer = QuestionSerializer(qs,many=True)
    return Response(serializer.data)


def quiz_list(request):
    quizzes = Quiz.objects.all().select_related('creator').prefetch_related('question')
    return render(request,'quiz/quiz_list.html',{'quizzes':quizzes})

class CreatorCreateApiView(generics.CreateAPIView,generics.ListAPIView):
    queryset =  Creator.objects.all()
    serializer_class = CreatorSerializer



    def post(self,request,*args,**kwargs):
        data = request.data
        username = data['username']
        print(username)
        try:
            Creator.objects.create(username=username)
            'This username already exists,choose another one!'    
        except IntegrityError:
            return render(request, 'quiz/names.html', {'message':'This username already exists,choose another one!'}) 
       