
from django.db import models
from django.db.models import Sum
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
    user = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,default=1)
    question_length = models.IntegerField()
    
    def __str__(self):
        return f"user : {self.user}   scored  {self.score} out of {self.question_length}" 

    @property
    def passed_or_failed(self):
        if self.score>self.question_length*0.6:
            return True
        else:
            return False

class Visitor(models.Model):
    visitor =  models.CharField(max_length=250)

    def __str__(self):
        return str(self.visitor)