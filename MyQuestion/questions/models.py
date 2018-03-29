from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
	def sort_date(self):
		result_list = Question.objects.order_by('date')[:5]
		return result_list
	def sort_hot(self):
		result_list = Question.objects.order_by('-rating')
		return result_list
	def by_tag(self, tagw):
		result_list = Question.objects.filter(tags__word=tagw)
		return result_list

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
	objects = QuestionManager()
	def __str__(self):
		return self.title

class Answer(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField(max_length=500)
	rating = models.IntegerField(default=0)
	correct = models.BooleanField(default=False)
	date = models.DateTimeField()
	question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE)
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
	def get_avatar_path(self):
		return self.avatar
