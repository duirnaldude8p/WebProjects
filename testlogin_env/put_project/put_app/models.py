from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

def profile_image_path(instance, filename):
    return os.path.join('', str(instance.id), filename)

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User)
	profile_pic = models.ImageField(upload_to=profile_image_path, blank=True)

	def __str__(self):
		return self.user.username


# class Put(models.Model):
# 	user = models.OneToOneField(User)
# 	my_name = models.CharField(default="", blank=True, null=True, max_length=20)
# 	# profile_pic = models.ImageField(upload_to=profile_image_path, blank=True)

# 	def __str__(self):
# 		return self.user.username
