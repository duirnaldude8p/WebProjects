from rest_framework import serializers

import json

from .models import UserProfileInfo

from .forms import UserForm
from .forms import UserProfileInfoForm

class RegisterSerializer(serializers.ModelSerializer):
	# user = serializers.PrimaryKeyRelatedField(read_only=True)
	username = serializers.CharField(source='user.username')

	class Meta:
		model = UserProfileInfo

		fields = ('__all__')

	def create(self, validated_data):
		profile = UserProfileInfo.objects.create(
			username = validated_data['username'],
			profile_pic = validated_data['profile_pic'],
		)

	
		return profile 

	def update(self, instance, validated_data):
		instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
		instance.save()
		return instance

class ProfileSerializer(serializers.ModelSerializer):
	# user = serializers.PrimaryKeyRelatedField(read_only=True)
	username = serializers.CharField(source='user.username')

	class Meta:
		model = UserProfileInfo

		fields = ('__all__')

	def create(self, validated_data):
		profile = UserProfileInfo
		section = validated_data['section']
		post = validated_data['test_data']
		
		if section == "test post":
			print("POST RECIEVED: %s"%post)

		return profile 

	def update(self, instance, validated_data):
		instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
		instance.save()
		return instance





