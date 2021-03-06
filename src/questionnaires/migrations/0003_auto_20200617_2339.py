# Generated by Django 3.0.7 on 2020-06-17 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionnaires', '0002_auto_20200612_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='score',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='result',
            name='questionnaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionnaires.Questionnaire'),
        ),
        migrations.AddField(
            model_name='result',
            name='score_lower',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='result',
            name='score_upper',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='quiz_title',
            field=models.CharField(default='test', max_length=255),
        ),
    ]
