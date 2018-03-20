from django.db import models
from django.db.models import ImageField, FileField, signals
from django.dispatch import dispatcher
from django.conf import settings
import shutil, os, glob, re
from distutils.dir_util import mkpath
import uuid

# Create your models here.

def cat_image_path(instance, filename):
    return os.path.join('static/pics/cats', str(instance.id), filename)

def profile_image_path(instance, filename):
    return os.path.join('static/pics/profile', str(instance.id), filename)

def image_path(instance, filename):
    return os.path.join('static/pics/main', str(instance.id), filename)

# class CustomImageField(ImageField):
#     """Allows model instance to specify upload_to dynamically.

#     Model class should have a method like:

#         def get_upload_to(self, attname):
#             return 'path/to/{0}'.format(self.id)
#     """
#     def __init__(self, *args, **kwargs):
#         kwargs['upload_to'] = kwargs.get('upload_to', 'image_path')

#         try:
#             self.use_key = kwargs.pop('use_key')
#         except KeyError:
#             self.use_key = False

#         super(CustomImageField, self).__init__(*args, **kwargs)

#     def contribute_to_class(self, cls, name):
#         """Hook up events so we can access the instance."""
#         super(CustomImageField, self).contribute_to_class(cls, name)
#         dispatcher.connect(self._move_image, signal=signals.post_save, sender=cls)

#     def _move_image(self, instance=None):
#     	"""
#             Function to move the temporarily uploaded image to a more suitable directory 
#             using the model's get_upload_to() method.
#         """
#         if hasattr(instance, 'get_upload_to'):
#             src = getattr(instance, self.attname)
#             if src:
#                 m = re.match(r"%s/(.*)" % self.upload_to, src)
#                 if m:
#                     if self.use_key:
#                         dst = "%s/%d_%s" % (instance.get_upload_to(self.attname), instance.id, m.groups()[0])
#                     else:
#                         dst = "%s/%s" % (instance.get_upload_to(self.attname), m.groups()[0])
#                     basedir = "%s%s/" % (settings.MEDIA_ROOT, os.path.dirname(dst))
#                     mkpath(basedir)
#                     shutil.move("%s%s" % (settings.MEDIA_ROOT, src),"%s%s" % (settings.MEDIA_ROOT, dst))
#                     setattr(instance, self.attname, dst)
#                     instance.save()

#     def db_type(self):
#         """Required by Django for ORM."""
#         return 'varchar(100)'

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
	cat_user = models.IntegerField(default=1, null=True)
	get_id = models.CharField(max_length=10, null=True)
	section = models.CharField(max_length=20, null=True)
	category = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.cat_name

	def cat_id(self):
		return self.id

class Account(models.Model):
	account_user = models.IntegerField(default=1, null=True)
	profile_pic = models.ImageField(upload_to=profile_image_path, blank=True, null=True)
	cats = models.CharField(max_length=1000, null=True)
	cat_comments = models.CharField(max_length=1000, null=True)
	comments = models.CharField(max_length=1000, null=True)
	account_name = models.CharField(max_length=20, null=True)
	get_id = models.CharField(max_length=10, null=True)
	section = models.CharField(max_length=20, null=True)
	category = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.account_name

	def account_id(self):
		return self.id
	
class Main(models.Model):
	main_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	home_pic = models.ImageField(upload_to=image_path, blank=True, null=True)
	cats = models.CharField(max_length=1000, null=True)
	cat_comments = models.CharField(max_length=1000, null=True)
	comments = models.CharField(max_length=1000, null=True)
	accounts = models.CharField(max_length=1000, null=True)
	get_id = models.CharField(max_length=10, null=True)
	section = models.CharField(max_length=20, null=True)
	category = models.CharField(max_length=20, null=True)

	def __str__(self):
		return "Main"

	def main_id(self):
		return self.id