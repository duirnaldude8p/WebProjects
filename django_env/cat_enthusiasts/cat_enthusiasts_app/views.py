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
from .serializers import MainSerializer

# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required 

# from django.contrib.auth.models import User
# from rest_framework import authentication
# from rest_framework import exceptions

# class UserLogin(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         username = request.META.get('username')
#         password = request.META.get('username')
#         if not username and not password:
#             return None

#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such user')

#         return (user, None)




def main(request):
	return render(request, "home.html")

def profile(request):
	return render(request, "profile.html", {})

def bigcatlist(request):
	return render(request, "bigcatlist.html", {})

def bigcat(request):
	return render(request, "bigcat.html", {})

def my_user_login(request):
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

	
	# one_objs = One.objects.all().prefetch_related('many_set')
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


class MainGetData(generics.RetrieveAPIView):
	queryset = Main.objects.all()
	serializer_class = MainSerializer

	def get(self, request):
		queryset = Main.objects.all()
		serializer_class = MainSerializer(queryset, many=True)
		
		return Response(serializer_class.data)

	
class MainPostData(generics.CreateAPIView):
	queryset = Main.objects.all()
	serializer_class = MainSerializer
	
	print("in postdata")
	def post(self, request):
		serializer_class = MainSerializer(data=request.data)
		if serializer_class.is_valid():
			print("in is valid ")
			#serializer_class.create(serializer_class.validated_data)
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		print("errors: %s"%serializer_class._errors)
		return Response(serializer_class._errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.
