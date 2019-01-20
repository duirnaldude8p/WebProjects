from django.db import models

from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
	user = models.OnetoOneField(User, primary_key=True, on_delete=models.CASCADE)
	profile = models.ImageField(upload_to="profile_pics", blank=True, null=True)

	def __str__(self):
		return self.user.username
