from django.shortcuts import render
from .models import Quiz,Question,Choice
# Create your views here.

def index(request):
    quiz = Quiz.objects.select_related('creator').prefetch_related('question')
    return render(request,'quiz/index.html',{'quiz':quiz})