from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
	word = models.CharField(max_length=20)
	def __str__(self):
		return self.word

class Question(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	text = models.TextField(max_length=500)
	rating = models.IntegerField(default=0)
	date = models.DateTimeField()
	tags = models.ManyToManyField(Tag)
	def __str__(self):
		return self.title

class Answer(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField(max_length=500)
	rating = models.IntegerField(default=0)
	correct = models.BooleanField(default=False)
	date = models.DateTimeField()
	def __str__(self):
		return self.text

class Profile(models.Model):
	nickname = models.CharField(max_length=20)
	avatar = models.ImageField()
	date = models.DateTimeField()
	rating = models.IntegerField(default=0)
	user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
	def __str__(self):
		return self.nickname
