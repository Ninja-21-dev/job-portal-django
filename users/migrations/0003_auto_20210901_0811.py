# Generated by Django 3.2.7 on 2021-09-01 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_jobseeker_is_jobseeker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='is_employer',
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='is_jobseeker',
            field=models.BooleanField(default=True),
        ),
    ]
