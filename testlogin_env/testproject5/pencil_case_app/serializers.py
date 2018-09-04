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
		
		pencilcase = PencilCase.objects.create(
			pencil = validated_data['pencil'],
			rubber = validated_data['rubber'],
			pen = validated_data['pen'],
		)
		
		pencilcase.save()
		return pencilcase

	def update(self, instance, validated_data):
		# attr = validated_data.get('my_field', instance)
		attr = instance.name
		# attr = validated_data.get('my_field', instance.pencil)
		if attr == "pencil":
			instance.pencil = validated_data.get('pencil', instance.pencil)
		elif attr == "rubber":
			instance.rubber = validated_data.get('rubber', instance.rubber)
		elif attr == "pen":
			instance.pen = validated_data.get('pen', instance.pen)

		test_pencil = validated_data.get('pencil', instance.pencil)
		print("serializer pencil: %s id: %s isfield: %s"%(instance.pencil, instance.id, attr))
		instance.save()
		return instance