# Generated by Django 4.1.6 on 2023-02-10 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Holmes", "0013_remove_jobs_skills_jobs_skills"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="jobs_applied",
        ),
        migrations.AddField(
            model_name="user",
            name="jobs_applied",
            field=models.ManyToManyField(blank=True, null=True, to="Holmes.jobs"),
        ),
    ]
