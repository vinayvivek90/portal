from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	email = models.EmailField(max_length=254, default = 'admin@aviate.com')
	location = models.CharField(max_length = 254, default= 'Bangalore')
	
class Resume(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	path = models.FileField()
	uploaded = models.DateTimeField(auto_now=True)
