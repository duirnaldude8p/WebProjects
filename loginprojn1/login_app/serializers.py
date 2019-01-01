from rest_framework import serializers

from .models import UserProfileInfo
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfileInfo
		fields = ('__all__')

	def create(self, validated_data):
		print("create user profile: %s"%validated_data.get('username'))

		# user = User.objects.create_user(
		#  	username = validated_data.get('username'),
  #           password = validated_data.get('password')
  #       )

		# user.save()

		# if 'profile_pic' in request.FILES:
		# 	print('found it')
		# 	profile_pic = request.FILES['profile_pic']

		# profile = UserProfileInfo.objects.create(
		# 	user = user,
		# 	profile_pic = profile_pic,			
		# )
		# # profile.save(commit=False)

		# # profile.user = user

		# profile.save()

		return profile
		

class ProfileSerializer2(serializers.ModelSerializer):

	class Meta:
		model = UserProfileInfo
		fields = ('__all__')