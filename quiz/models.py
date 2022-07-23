from pickle import FALSE, TRUE
from django.db import models

# Create your models here.





class Question(models.Model):
    question = models.CharField(max_length=250)
    @property
    def get_answers(self):
        return self.choice_set.all()

    def __str__(self):
        return self.question

class Choice(models.Model):
    option = models.CharField(max_length=30)
    correct = models.BooleanField(default=False) 
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='options')
    def __str__(self):
        return self.option

class Creator(models.Model):
    username = models.CharField(max_length=30)
   
    def __str__(self):
        return str(self.username)
class Quiz(models.Model):
    question = models.ManyToManyField(Question)
    creator = models.ForeignKey(Creator,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.creator.username
   
    class Meta:
         verbose_name_plural = "Quizzes"

class Result(models.Model):
    score = models.IntegerField(blank=False)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)