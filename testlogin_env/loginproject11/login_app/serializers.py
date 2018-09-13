from rest_framework import serializers

from .models import UserProfileInfo
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfileInfo
		fields = ('__all__')

	def create(self, validated_data):
		print("create user profile: %s"%validated_data.get('username'))

		user = User.objects.create_user(
		 	username = validated_data.get('username'),
            password = validated_data.get('password')
        )

		user.save()

		profile = UserProfileInfo.objects.create(
			user = user,
			username = "_user_",
			password = "_user_",
			profile_pic = validated_data['profile_pic'],			
		)
		# profile.save(commit=False)

		# profile.user = user

		profile.save()

		return profile
		

class ProfileSerializer2(serializers.ModelSerializer):

	class Meta:
		model = UserProfileInfo
		fields = ('__all__')