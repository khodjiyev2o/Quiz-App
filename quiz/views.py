from urllib import response
from django.db import IntegrityError
from django.shortcuts import render,redirect
from .models import Quiz,Question,Choice,Creator,Result
from .serializers import QuestionSerializer,CreatorSerializer,ResultSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from quiz import serializers
from rest_framework import generics

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
            Creator.objects.create(username=username)
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

    

       
    
