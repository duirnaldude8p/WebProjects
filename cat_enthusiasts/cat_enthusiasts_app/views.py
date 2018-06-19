from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .models import Cat
from .models import Profile
from .models import Main
from .models import Comment

from .serializers import ProfileSerializer


def main(request):
	return render(request, "home.html", {})

def profile(request):
	return render(request, "profile.html", {})

def bigcatlist(request):
	return render(request, "bigcatlist.html", {})

def bigcat(request):
	return render(request, "bigcat.html", {})

def login(request):
	return render(request, "login.html", {})

def register(request):
	return render(request, "register.html")

class ProfileGetData(generics.RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

	def get(self, request):
		queryset = Profile.objects.all()
		serializer_class = ProfileSerializer(queryset, many=True)
		
		return Response(serializer_class.data)

	
class ProfilePostData(generics.CreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	
	print("in postdata")
	def post(self, request):
		serializer_class = ProfileSerializer(data=request.data)
		if serializer_class.is_valid():
			print("in is valid ")
			#serializer_class.create(serializer_class.validated_data)
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		print("errors: %s"%serializer_class._errors)
		return Response(serializer_class._errors, status=status.HTTP_400_BAD_REQUEST)






# Create your views here.
