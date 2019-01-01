from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from .serializers import ProfileSerializer
from .serializers import ProfileSerializer2

from .models import UserProfileInfo


def login(request):
	return render(request, 'login_app/login.html')

def register(request):
	return render(request, 'login_app/register.html')

def profile(request):
	return render(request, 'login_app/profile.html')

class GetProfileData(generics.RetrieveAPIView):
	queryset = UserProfileInfo.objects.all()
	serializer_class = ProfileSerializer

	def get(self, request):
		queryset = UserProfileInfo.objects.all()
		serializer_class = ProfileSerializer(queryset, many=True)

		return Response(serializer_class.data)

class PostProfileData(generics.CreateAPIView):
	queryset = UserProfileInfo.objects.all()
	serializer_class = ProfileSerializer

	def post(self, request):
		serializer_class = ProfileSerializer(data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class PostProfileData2(generics.CreateAPIView):
	queryset = UserProfileInfo.objects.all()
	serializer_class = ProfileSerializer2

	def post(self, request):
		serializer_class = ProfileSerializer2(data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)





