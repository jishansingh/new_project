from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
# Create your models here.
from.choices import *

class blog(models.Model):
	data=models.TextField()
	
class topic(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=30)
	blog=models.ManyToManyField(blog,blank=True)
	date = models.DateField(("Date"), default=datetime.date.today)
	def __str__(self):
		return self.title
class url_post(models.Model):
	url=models.CharField(max_length=100)
	name=models.CharField(max_length=50)
	visited=models.IntegerField(default=0)
	visitors=models.ManyToManyField(User,blank=True)
	def __str__(self):
		return self.name


class called(models.Model):
	visited=models.IntegerField(default=0)
	visitors=models.ManyToManyField(User,blank=True)
class other_photos(models.Model):
	image=models.FileField()
class visited(models.Model):
	visited=models.IntegerField(default=0)
	visitors=models.ManyToManyField(User,blank=True)
class product(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=50)
	image=models.FileField()
	category=models.CharField(max_length=50,choices=CHOICE,default="cars")
	other=models.ManyToManyField(other_photos,blank=True)
	desciption=models.TextField()
	phone_number=models.IntegerField(default=0)
	name=models.CharField(max_length=50)
	date = models.DateField(("Date"), default=datetime.date.today)
	called=models.OneToOneField(called,on_delete=models.CASCADE)
	visited=models.OneToOneField(visited,on_delete=models.CASCADE)
	def __str__(self):
		return self.title


