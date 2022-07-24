from urllib import response

from django.db import IntegrityError
from django.shortcuts import redirect, render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from quiz import serializers

from .models import Choice, Creator, Question, Quiz, Result,Visitor
from .serializers import (CreatorSerializer, QuestionSerializer,
                          ResultSerializer)

# Create your views here.

def index(request):
    quiz = Quiz.objects.filter(id=1).select_related('creator').prefetch_related('question')
    return render(request,'quiz/index.html',{'quiz':quiz})
    

def names(request):
    return render(request,'quiz/names.html',{})


def results(request):
    results = Result.objects.select_related('quiz').order_by('-score').filter(quiz=1)
    return render(request,'quiz/result.html',{'results':results})


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
            Visitor.objects.create(visitor=username)
            'This username already exists,choose another one!'    
        except IntegrityError:
            return render(request, 'quiz/names.html', {'message':'This username already exists,choose another one!'}) 

        return Response("done")

class ResultCreateApiView(generics.CreateAPIView,generics.ListAPIView):
    queryset =  Result.objects.all()
    serializer_class = ResultSerializer

    def post(self,request,*args,**kwargs):
        data = request.data
        user = data['user']
        score = data['score']
        
        quiz = Quiz.objects.first()
       
        obj, created = Result.objects.update_or_create(
        user=user, quiz=quiz,
        defaults={'score': score},
    )
        

        return Response("hi")

    

       
    
