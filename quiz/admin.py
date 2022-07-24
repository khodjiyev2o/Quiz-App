from django.contrib import admin

from .models import Choice, Creator, Question, Quiz, Result, Visitor

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Quiz)
admin.site.register(Creator)
admin.site.register(Result)
admin.site.register(Visitor)
