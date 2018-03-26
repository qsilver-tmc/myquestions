from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	text = models.TextField()
	rating = models.IntegerField(default=0)
