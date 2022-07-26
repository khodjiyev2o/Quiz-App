
from django.urls import path
from . import views
urlpatterns = [
    path('index/quiz',views.index,name='index'),
    path('quiz_list',views.quiz_list,name='quiz_list'),
    path('results',views.results,name='results'),
    path('api/questions',views.api_questions),
    path('api/visitors',views.CreatorCreateApiView.as_view(),name="visitors"),
    path('api/results',views.ResultCreateApiView.as_view(),name="results_api"),
    path('',views.names,name='names'),
]
