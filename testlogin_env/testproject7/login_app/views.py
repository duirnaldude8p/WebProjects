from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from .serializers import ProfileSerializer

from .models import UserProfileInfo

def login(request):
	return render(request, 'pencilcase_creator.html')

def register(request):
	return render(request, 'pencilcases.html')

def profile(request):
	return render(request, 'pencilcases.html')

class GetPencilCaseData(generics.RetrieveAPIView):
	queryset = PencilCase.objects.all()
	serializer_class = PencilCaseSerializer

	def get(self, request):
		queryset = PencilCase.objects.all()
		serializer_class = PencilCaseSerializer(queryset, many=True)

		return Response(serializer_class.data)
