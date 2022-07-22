from pickle import TRUE
from django.db import models

# Create your models here.





class Question(models.Model):
    text = models.CharField(max_length=30)
    @property
    def get_answers(self):
        return self.choice_set.all()

    def __str__(self):
        return self.text

class Choice(models.Model):
    text = models.CharField(max_length=30)
    correct = models.BooleanField(default=False) 
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choices')
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
