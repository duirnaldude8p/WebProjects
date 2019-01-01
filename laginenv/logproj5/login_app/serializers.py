from rest_framework import serializers

from .models import UserProfileInfo
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfileInfo
		fields = ('__all__')

	def create(self, validated_data):
		print("create user profile: %s"%validated_data.get('username'))

		profile = UserProfileInfo.objects.create(
			username = validated_data.get('username'),
            password = validated_data.get('password')			
		)

		profile.save()

		return profile
		