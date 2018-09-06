from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics
from rest_framework import status


from django.contrib.auth.models import User
from .models import UserProfileInfo
from .serializers import ProfileSerializer



from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def userlogin(request):
	return render(request,'login_app/login.html')

def userregister(request):
	return render(request,'login_app/register.html')

def userprofile(request):
	return render(request,'login_app/profile.html')

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
			print("post view user object usrnm: %s"%UserProfileInfo.objects.get(username="sam").username)
			return Response(serializer_class.data, status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status.HTTP_400_BAD_REQUEST)

