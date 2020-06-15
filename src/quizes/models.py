from django.db import models


class Quiz(models.Model):
    quiz_title = models.CharField(max_length=200, default='test')

    def __str__(self):
        return self.quiz_title


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.choice_text


class Result(models.Model):
    result_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.result_text
