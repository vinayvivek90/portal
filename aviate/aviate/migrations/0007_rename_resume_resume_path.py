# Generated by Django 3.2.8 on 2021-10-31 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aviate', '0006_alter_resume_uploaded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='resume',
            new_name='path',
        ),
    ]
