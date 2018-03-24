from django.db import models
from django.conf import settings
import os


# Create your models here.

def cat_image_path(instance, filename):
    return os.path.join('CatApp3\static\pics\cats', str(instance.id), filename)

def profile_image_path(instance, filename):
    return os.path.join('CatApp3\static\pics\profile', str(instance.id), filename)

def image_path(instance, filename):
    return os.path.join('CatApp3\static\pics\main', str(instance.id), filename)



class Cat(models.Model):
	cat_name = models.CharField(max_length=20, null=True)
	breed = models.CharField(max_length=20, null=True)
	story = models.CharField(max_length=140, null=True)
	cat_pic = models.ImageField(upload_to=cat_image_path, blank=True, null=True)
	cat_comments = models.CharField(max_length=1000, null=True)
	cat_user = models.IntegerField(default=1, null=True)
	get_id = models.CharField(max_length=10, null=True)
	section = models.CharField(max_length=20, null=True)
	category = models.CharField(max_length=20, null=True)

	def save(self, *args, **kwargs):
		if self.id is None:
			saved_image = self.cat_pic
			self.cat_pic = None
			super(Cat, self).save(*args, **kwargs)
			self.cat_pic = saved_image
			kwargs.pop('force_insert')

			super(Cat, self).save(*args, **kwargs)

	def __str__(self):
		return self.cat_name

	def cat_id(self):
		return self.id

class Account(models.Model):
	username = models.CharField(max_length=20, null=True)
	password = models.CharField(max_length=20, null=True)
	profile_pic = models.ImageField(upload_to=profile_image_path, blank=True, null=True)
	cats = models.CharField(max_length=1000, null=True)
	cat_comments = models.CharField(max_length=1000, null=True)
	comments = models.CharField(max_length=1000, null=True)
	account_name = models.CharField(max_length=20, null=True)
	get_id = models.CharField(max_length=10, null=True)
	section = models.CharField(max_length=20, null=True)
	category = models.CharField(max_length=20, null=True)

	def save(self, *args, **kwargs):
		if self.id is None:
			saved_image = self.profile_pic
			self.profile_pic = None
			super(Account, self).save(*args, **kwargs)
			self.profile_pic = saved_image
			kwargs.pop('force_insert')

			super(Account, self).save(*args, **kwargs)

	def __str__(self):
		return self.account_name

	def account_id(self):
		return self.id
	
class Main(models.Model):
	home_pic = models.ImageField(upload_to=image_path, blank=True, null=True)
	cats = models.CharField(max_length=1000, null=True)
	cat_comments = models.CharField(max_length=1000, null=True)
	comments = models.CharField(max_length=1000, null=True)
	accounts = models.CharField(max_length=1000, null=True)
	get_id = models.CharField(max_length=10, null=True)
	section = models.CharField(max_length=20, null=True)
	category = models.CharField(max_length=20, null=True)

	def save(self, *args, **kwargs):
		if self.id is None:
			saved_image = self.home_pic
			self.home_pic = None
			super(Main, self).save(*args, **kwargs)
			self.home_pic = saved_image
			kwargs.pop('force_insert')

			super(Main, self).save(*args, **kwargs)

	def __str__(self):
		return "Main"

	def main_id(self):
		return self.id
# Create your models here.
