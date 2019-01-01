from django.db import models

from django.contrib.auth.models import User




class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	# username = models.CharField(max_length=20, default="dude", blank=True, null=True)
	# made possible by installing pillow
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True, null=True)


	def __str__(self):
		return self.user.username



