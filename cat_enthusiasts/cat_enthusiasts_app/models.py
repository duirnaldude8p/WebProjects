from django.db import models
from django.conf import settings
import os

# Create your models here.

def cat_image_path(instance, filename):
    return os.path.join('cat_enthusiasts_app\static\pics\cats', str(instance.id), filename)

def profile_image_path(instance, filename):
    return os.path.join('cat_enthusiasts_app\static\pics\profile', str(instance.id), filename)

# def image_path(instance, filename):
#     return os.path.join('catpageapp\static\pics\main', str(instance.id), filename)

class Main(models.Model):
	name = models.CharField(max_length=20, null=True)
	section = models.CharField(max_length=20, null=True)
	
	def __str__(self):
		return self.name	


class Profile(models.Model):
	# comment = models.OneToOneField(Comment, on_delete=models.CASCADE, null=True)
	# cat = models.OneToOneField(Cat, on_delete=models.CASCADE, null=True)
	main = models.ForeignKey(Main, on_delete=models.CASCADE, null=True)
	username = models.CharField(max_length=30, null=True)
	password = models.CharField(max_length=20, null=True)
	profile_pic = models.ImageField(upload_to=profile_image_path, blank=True, null=True)
	profile_name = models.CharField(max_length=15, null=True)
	get_id = models.CharField(max_length=10, null=True, default='')
	section = models.CharField(max_length=20, null=True)
	# category = models.CharField(max_length=20, null=True)

	def save(self, *args, **kwargs):
		if self.id is None:
			saved_image = self.profile_pic
			self.profile_pic = None
			super(Profile, self).save(*args, **kwargs)
			self.profile_pic = saved_image
			kwargs.pop('force_insert')

			super(Profile, self).save(*args, **kwargs)

	def __str__(self):
		return self.profile_name

	def profile_id(self):
		return self.id

class Comment(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	main = models.ForeignKey(Main, on_delete=models.CASCADE, null=True)
	text = models.CharField(max_length=140, null=True)
	is_remove = models.NullBooleanField(default=False, null=True)

class Cat(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	main = models.ForeignKey(Main, on_delete=models.CASCADE, null=True)
	cat_name = models.CharField(max_length=20, null=True)
	breed = models.CharField(max_length=30, null=True)
	story = models.CharField(max_length=140, null=True)
	cat_pic = models.ImageField(upload_to=cat_image_path, blank=True, null=True)
	is_remove = models.NullBooleanField(default=False, null=True)
	# cat_comments = models.CharField(max_length=100000, null=True)
	# get_id = models.CharField(max_length=10, null=True, default='')
	# section = models.CharField(max_length=20, null=True)
	# category = models.CharField(max_length=20, null=True)
	# cat_unique_id = models.CharField(max_length=20, null=True, default="")
	# name = models.CharField(max_length=30, blank=True, null=True)
	# picture = models.CharField(max_length=100, blank=True, null=True)

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



