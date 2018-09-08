from rest_framework import serializers

from .models import UserProfileInfo
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfileInfo
		fields = ('__all__')

	def create(self, validated_data):
		print("hello create user profile: %s"%validated_data.get('usrnm'))

		user = User.objects.create_user(
		 	validated_data.get('usrnm'),
            validated_data.get('pwd')
        )

		user.save()

		profile = UserProfileInfo.objects.create(
			# user = user,
			profile_pic = validated_data['profile_pic'],			
		)
		profile.save(commit=False)

		# profile.user = user

		profile.save()

		return profile
		