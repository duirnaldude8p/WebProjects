from rest_framework import serializers

from .models import PencilCase

class PencilCaseSerializer(serializers.ModelSerializer):
	pencil = serializers.CharField(default="", max_length=15)
	rubber = serializers.CharField(default="", max_length=15)
	pen = serializers.CharField(default="", max_length=15)
	
	class Meta:
		model = PencilCase
		fields = ('__all__')

	def create(self, validated_data):
		print("hello create pencil")
		pencilcase = PencilCase.objects.create(
			pencil = validated_data['pencil'],
			rubber = validated_data['rubber'],
			pen = validated_data['pen'],
		)
		
		pencilcase.save()
		return pencilcase

	def update(self, instance, validated_data):
		
		instance.pencil = validated_data.get('pencil', instance.pencil)
		instance.rubber = validated_data.get('rubber', instance.rubber)
		instance.pen = validated_data.get('pen', instance.pen)

		instance.save()
		return instance