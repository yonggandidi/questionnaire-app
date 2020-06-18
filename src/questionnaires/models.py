from django.db import models
from datetime import datetime


class Questionnaire(models.Model):
    quiz_title = models.CharField(max_length=255, default='test')
    author = models.ForeignKey(
        'authentication.MyUser', on_delete=models.CASCADE, related_name='questionnaire', null=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quiz_title


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    questionnaire = models.ForeignKey(
        Questionnaire, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(default=None)

    def __str__(self):
        return self.choice_text


class Result(models.Model):
    result_text = models.CharField(max_length=10000)
    questionnaire = models.ForeignKey(
        Questionnaire, on_delete=models.CASCADE, null=True)
    score_upper = models.IntegerField(default=0)
    score_lower = models.IntegerField(default=0)

    def __str__(self):
        return self.result_text
