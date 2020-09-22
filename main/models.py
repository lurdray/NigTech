from django.db import models
from django.utils import timezone


# Create your models here.

class Work(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	description = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

class ContactModel(models.Model):
	"""docstring for ContactModel"""
	name = models.CharField(max_length=60, default="none")
	email = models.CharField(max_length=60, default="none")
	phone = models.CharField(max_length=60, default="none")
	message = models.CharField(max_length=60, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name