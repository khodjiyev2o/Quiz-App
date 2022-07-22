from pickle import TRUE
from django.db import models

# Create your models here.


class Choice(models.Model):
    text = models.CharField(max_length=30)   
    def __str__(self):
        return self.text



class Question(models.Model):
    text = models.CharField(max_length=30)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(Choice,on_delete=models.CASCADE,related_name='answer')
    def __str__(self):
        return self.text

class Creator(models.Model):
    username = models.CharField(unique=True,max_length=30)
    def __str__(self):
        return str(self.username)
class Quiz(models.Model):
    question = models.ManyToManyField(Question)
    creator = models.ForeignKey(Creator,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.creator.username
   
    class Meta:
         verbose_name_plural = "Quizzes"
