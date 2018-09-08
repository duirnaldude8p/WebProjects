from django.db import models
from django.contrib.auth.models import User
import os

# def profile_image_path(instance, filename):
#     return os.path.join('', str(instance.id), filename)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}'.format(instance.id)

class UserProfileInfo(models.Model):
	# user = models.OneToOneField(User)
	# test_text = models.CharField(max_length=20, null=True, blank=True)
	usrnm = models.CharField(unique=True, max_length=20, null=True, blank=True)
	pwd = models.CharField(max_length=20, null=True, blank=True)
	profile_pic = models.ImageField(upload_to=user_directory_path, blank=True)

	def __str__(self):
		return "profile"

	def save(self, *args, **kwargs):
		if self.pk is None:
			saved_image = self.profile_pic
			self.profile_pic = None
			super(UserProfileInfo, self).save(*args, **kwargs)
			self.profile_pic = saved_image

		super(UserProfileInfo, self).save(*args, **kwargs)

	
 
# Create your models here.
