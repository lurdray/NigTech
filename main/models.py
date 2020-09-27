from django.db import models
from django.utils import timezone


# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=160, default="none")
	country = models.CharField(max_length=160, default="none")
	position = models.CharField(max_length=60, default="none")
	facebook = models.CharField(max_length=160, default="none")
	twitter = models.CharField(max_length=160, default="none")
	instagram = models.CharField(max_length=160, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Work(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=160, default="none")
	link = models.CharField(max_length=160, default="none")
	image = models.ImageField(upload_to='images')
	description = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

class ContactModel(models.Model):
	"""docstring for ContactModel"""
	name = models.CharField(max_length=160, default="none")
	email = models.CharField(max_length=160, default="none")
	phone = models.CharField(max_length=60, default="none")
	message = models.CharField(max_length=1060, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name




class DigitalMarketer(models.Model):
	name = models.CharField(max_length=160, default="none")
	email = models.CharField(max_length=160, default="none")
	phone = models.CharField(max_length=60, default="none")
	about = models.TextField()
	why = models.TextField()
	address = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name