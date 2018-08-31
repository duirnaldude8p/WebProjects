from django.db import models
from django.contrib.auth.models import User
import os

from django.db.models import ImageField, FileField, signals
from django.dispatch import dispatcher
from django.conf import settings
import shutil, os, glob, re
from distutils.dir_util import mkpath
from django.dispatch import Signal
# Create your models here.


class UserProfileInfo(models.Model):
	user = models.OneToOneField(User)
	profile_pic = models.ImageField(upload_to="images", blank=True)

	def __str__(self):
		return self.user.username


