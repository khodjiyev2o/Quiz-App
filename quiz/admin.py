from django.contrib import admin
from .models import Choice,Question,Quiz,Creator
# Register your models here.



admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Creator)
