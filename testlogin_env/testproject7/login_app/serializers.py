from rest_framework import serializers

from .models import UserProfileInfo

class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfileInfo
		fields = ('__all__')

	def create(self, validated_data):
		print("hello create")
		