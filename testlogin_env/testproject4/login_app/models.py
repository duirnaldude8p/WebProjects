from django.db import models
from django.contrib.auth.models import User
import os

# def profile_image_path(instance, filename):
#     return os.path.join('', str(instance.id), filename)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, "images")

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User)
	profile_pic = models.ImageField(upload_to=user_directory_path, blank=True)

	def __str__(self):
		return self.user.username

	
 
# Create your models here.
