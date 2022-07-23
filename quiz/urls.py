
from django.urls import path
from . import views
urlpatterns = [
    path('index/<str:username>/quiz',views.index,name='index'),
    path('quiz_list',views.quiz_list,name='quiz_list'),
    path('api/questions',views.api_questions),
    path('api/creators',views.CreatorCreateApiView.as_view()),
    path('api/results',views.ResultCreateApiView.as_view()),
    path('',views.names,name='names'),
]
