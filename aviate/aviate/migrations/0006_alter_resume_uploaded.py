# Generated by Django 3.2.8 on 2021-10-31 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviate', '0005_alter_resume_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='uploaded',
            field=models.DateTimeField(auto_now=True),
        ),
    ]