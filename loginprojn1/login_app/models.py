from django.db import models
from django.contrib.auth.models import User

import os


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}'.format(instance.user.id)

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to=user_directory_path, blank=True)

	def __str__(self):
		return self.user.username

	def save(self, *args, **kwargs):
		if self.pk is None:
			saved_image = self.profile_pic
			self.profile_pic = None
			super(UserProfileInfo, self).save(*args, **kwargs)
			self.profile_pic = saved_image

		super(UserProfileInfo, self).save(*args, **kwargs)
