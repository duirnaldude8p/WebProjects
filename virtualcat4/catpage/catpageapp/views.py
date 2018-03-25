from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .models import Cat
from .models import Account
from .models import Main
from .models import CurrentAccount

from .serializers import CatSerializer
from .serializers import AccountSerializer
from .serializers import MainSerializer
from .serializers import CurrentAccountSerializer

import json

# Create your views here.

def main(request):
	return render(request, "Index.html", {})

def account(request):
	return render(request, "Account.html", {})

def catlist(request):
	return render(request, "CatList.html", {})

def catpage(request):
	return render(request, "CatPage.html", {})

def login(request):
	return render(request, "Login.html", {})

def register(request):
	return render(request, "Register.html")


class CatGetData(generics.RetrieveAPIView):
	queryset = Cat.objects.all()
	serializer_class = CatSerializer

	#print("cat queryset: %s"%queryset)
	
	def get(self, request):
		queryset = Cat.objects.all()
		serializer_class = CatSerializer(queryset, many=True)
		
		return Response(serializer_class.data)

class CatPostData(generics.CreateAPIView):
	queryset = Cat.objects.all()
	serializer_class = CatSerializer

	def post(self, request):
		serializer_class = CatSerializer(data=request.data, many=True)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountGetData(generics.RetrieveAPIView):
	queryset = Account.objects.all()
	serializer_class = AccountSerializer

	def get(self, request):
		queryset = Account.objects.all()
		serializer_class = AccountSerializer(queryset, many=True)
		
		return Response(serializer_class.data)

	
class AccountPostData(generics.CreateAPIView):
	queryset = Account.objects.all()
	serializer_class = AccountSerializer
	
	print("in postdata")
	def post(self, request):
		serializer_class = AccountSerializer(data=request.data)
		if serializer_class.is_valid():
			print("in is valid ")
			#serializer_class.create(serializer_class.validated_data)
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		print("errors: %s"%serializer_class._errors)
		return Response(serializer_class._errors, status=status.HTTP_400_BAD_REQUEST)

class CurrentAccountGetData(generics.RetrieveAPIView):
	queryset = CurrentAccount.objects.all()
	serializer_class = CurrentAccountSerializer

	def get(self, request):
		queryset = CurrentAccount.objects.all()
		serializer_class = CurrentAccountSerializer(queryset, many=True)
		
		return Response(serializer_class.data)

	
class CurrentAccountPostData(generics.CreateAPIView):
	queryset = CurrentAccount.objects.all()
	serializer_class = CurrentAccountSerializer

	def post(self, request):
		serializer_class = CurrentAccountSerializer(data=request.data)
		if serializer_class.is_valid():
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

	def post(self, request):
		serializer_class = MainSerializer(data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.



# Create your views here.
