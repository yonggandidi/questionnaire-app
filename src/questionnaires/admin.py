from django.contrib import admin
from .models import Question, Questionnaire, Choice

# Register your models here.
admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(Choice)
