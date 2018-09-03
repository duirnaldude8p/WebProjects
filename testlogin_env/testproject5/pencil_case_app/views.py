from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from .serializers import PencilCaseSerializer

from .models import PencilCase

def casecreator(request):
	return render(request, 'pencilcase_creator.html')

def pencilcases(request):
	return render(request, 'pencilcases.html')

class GetPencilCaseData(generics.RetrieveAPIView):
	queryset = PencilCase.objects.all()
	serializer_class = PencilCaseSerializer

	def get(self, request):
		queryset = PencilCase.objects.all()
		serializer_class = PencilCaseSerializer(queryset, many=True)

		return Response(serializer_class.data)

class PostPencilCaseData(generics.CreateAPIView):
	queryset = PencilCase.objects.all()
	serializer_class = PencilCaseSerializer

	def post(self, request):
		serializer_class = PencilCaseSerializer(data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status.HTTP_201_CREATED)
		return Response(serializer_class.error, status.HTTP_400_BAD_REQUEST)


class PutPencilCaseData(generics.UpdateAPIView):
	queryset = PencilCase.objects.all()
	serializer_class = PencilCaseSerializer

	def put(self, request, pk, format=None):
		pencil_case = self.get_object(pk)
		serializer_class = PencilCaseSerializer(pencil_case, data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
