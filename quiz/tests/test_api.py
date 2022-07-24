import json
from tkinter.messagebox import QUESTION

from django.contrib.auth.models import User
from django.urls import reverse
from quiz.models import Creator, Question, Quiz, Result, Visitor
from quiz.serializers import (CreatorSerializer, QuestionSerializer,
                              ResultSerializer)
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestApi(APITestCase):
    def setUp(self):
        question =  Question.objects.create(question="How old are you")
        creator =  Creator.objects.create(username="samandar")
       
        self.visitor_api_url = reverse('visitors')
        self.results_api_url = reverse('results')
        self.assertEqual(Visitor.objects.count(),0)
        self.question = Question.objects.get(question="How old are you")
        self.creator = Creator.objects.get(username="samandar")
        self.question = Question.objects.get(id=1)
        self.creator = Creator.objects.get(id=1)
       
        self.assertEquals(Question.objects.count(),1)
        self.assertEquals(Creator.objects.count(),1)
        self.quiz  = Quiz.objects.create(creator=creator)
        self.quiz.question.set([question])

    def test_visitor_api(self):    
        print(self.visitor_api_url)
        data= {'username':'me','id':'1'}
        response = self.client.post(self.visitor_api_url,data)
        self.assertEqual(Visitor.objects.count(),1)
        self.assertEquals(response.status_code,200)
        
    

    def test_results_api(self):
        data= {'user':'me','score':'5','quiz': self.quiz}
        response = self.client.post(self.results_api_url,data)
        result = Result.objects.get(score=5)
        self.assertEqual(Result.objects.count(),1)
        self.assertEqual(result.score,5)
        self.assertEqual(result.user,"me")
        self.assertEquals(response.status_code,200)
            