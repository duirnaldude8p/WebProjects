from django.db import models
from django.contrib.auth.models import User

def profile_image_path(instance, filename):
    return os.path.join('media\images\profile', str(instance.id), filename)

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User)
	profile_pic = models.ImageField(upload_to="images", blank=True)

	def __str__(self):
		return self.user.username
# Create your models here.

