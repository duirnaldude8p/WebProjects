from django.db import models
from django.conf import settings
import os

# Create your models here.

def cat_image_path(instance, filename):
    return os.path.join('static/pics/cats', str(instance.id), filename)

def profile_image_path(instance, filename):
    return os.path.join('static/pics/profile', str(instance.id), filename)

def image_path(instance, filename):
    return os.path.join('static/pics/main', str(instance.id), filename)

class Cat_Comment(models.Model):
	cat_comment = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.cat_comment

class Comment(models.Model):
	comment = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.comment

class User(models.Model):
	username = models.CharField(max_length=20, null=True)
	password = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.username

	def user_id(self):
		return self.id

class Cat(models.Model):
	cat_name = models.CharField(max_length=20, null=True)
	breed = models.CharField(max_length=20, null=True)
	story = models.CharField(max_length=140, null=True)
	cat_pic = models.ImageField(upload_to=cat_image_path, blank=True, null=True)
	cat_comments = models.CharField(max_length=1000, null=True)
	user = models.ForeignKey(User, unique=False, null=True)

	def __str__(self):
		return self.name

	def cat_id(self):
		return self.id

class Account(models.Model):
	user = models.ForeignKey(User, unique=False, null=True)
	profile_pic = models.ImageField(upload_to=profile_image_path, blank=True, null=True)
	cats = models.ForeignKey(Cat)
	cat_comments = models.ForeignKey(Cat_Comment)
	comments = models.ForeignKey(Comment)
	name = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.name

	def account_id(self):
		return self.id
	
class Main(models.Model):
	home_pic = models.ImageField(upload_to=image_path, blank=True, null=True)
	cats = models.ForeignKey(Cat)
	cat_comments = models.ForeignKey(Cat_Comment)
	comments = models.ForeignKey(Comment)
	accounts = models.ForeignKey(Account)


	def __str__(self):
		return "Main"

	def main_id(self):
		return self.id