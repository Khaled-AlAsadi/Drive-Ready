# Generated by Django 4.2.9 on 2024-03-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_question_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="traficruletext",
            name="video_link",
            field=models.CharField(max_length=500, null=True),
        ),
    ]
