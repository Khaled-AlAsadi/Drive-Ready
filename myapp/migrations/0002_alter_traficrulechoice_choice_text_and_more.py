# Generated by Django 4.2.9 on 2024-04-10 16:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="traficrulechoice",
            name="choice_text",
            field=models.CharField(
                max_length=200,
                validators=[
                    django.core.validators.MinLengthValidator(5),
                    django.core.validators.MaxLengthValidator(400),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="traficrulequestion",
            name="link",
            field=models.CharField(
                default="",
                max_length=500,
                validators=[
                    django.core.validators.MinLengthValidator(5),
                    django.core.validators.MaxLengthValidator(400),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="traficrulequestion",
            name="question_text",
            field=models.CharField(
                max_length=500,
                validators=[
                    django.core.validators.MinLengthValidator(5),
                    django.core.validators.MaxLengthValidator(400),
                ],
            ),
        ),
    ]
