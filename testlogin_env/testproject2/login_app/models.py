from django.db import models
from django.contrib.auth.models import User
import os

def profile_image_path(instance, filename):
    return os.path.join('', str(instance.id), filename)

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User)
	profile_pic = models.ImageField(upload_to=profile_image_path, blank=True)

	def __str__(self):
		return self.user.username

	# def save(self, *args, **kwargs):
	# 	if self.id is None:
	# 		saved_image = self.profile_pic
	# 		self.profile = None
	# 		super(UserProfileInfo, self).save(*args, **kwargs)
	# 		self.profile_pic = saved_image
	# 		# kwargs.pop('force_insert')

	# 		super(UserProfileInfo, self).save(*args, **kwargs)
	
# Create your models here.

