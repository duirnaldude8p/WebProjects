from rest_framework import serializers

from .models import UserProfileInfo
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
	print("hello serializer")
	username = serializers.CharField(source='user.username')
	# password = serializers.CharField(source='user.password')	
	# profile_pic = serializers.ImageField(required=False, max_length=None, 
 #                                     allow_empty_file=True, use_url=True)
	

	class Meta:
		model = UserProfileInfo
		fields = ('__all__')


	def create(self, validated_data):
		print("IN CREATE before")
		user = User
		user.username = validated_data['username']
		user.set_password(validated_data['password'])


		profile = UserProfileInfo.objects.create(
			profile_pic = validated_data['profile_pic'],
		)

		profile.user = user 
		profile.save()
		print("IN CREATE")
		return profile
