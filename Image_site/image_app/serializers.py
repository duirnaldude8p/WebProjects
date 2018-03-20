from rest_framework import serializers

import json

from .models import Picture

class PictureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Picture
		fields = ('__all__')