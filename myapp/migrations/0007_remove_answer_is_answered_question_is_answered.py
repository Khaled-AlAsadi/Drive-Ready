# Generated by Django 4.2.9 on 2024-03-27 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_remove_traficruletext_video_link"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="is_answered",
        ),
        migrations.AddField(
            model_name="question",
            name="is_answered",
            field=models.BooleanField(default=False),
        ),
    ]