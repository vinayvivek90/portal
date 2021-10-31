# Generated by Django 3.2.8 on 2021-10-30 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aviate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='resume',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='admin@aviate.com', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Bangalore', max_length=254),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='uploads/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
