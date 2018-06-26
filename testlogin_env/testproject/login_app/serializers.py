from rest_framework import serializers

import json

from .models import UserProfileInfo

from .forms import UserForm
from .forms import UserProfileInfoForm

class RegisterSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfileInfo

		fields = ('__all__')
	
	def create(self, validated_data):
		registered = False

		user_form = UserForm(data=validated_data)
		profile_form = UserProfileInfoForm(data=validated_data)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				print('profile pic found')

				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True
		else:
			print(user_form.errors, profile_form.errors)
