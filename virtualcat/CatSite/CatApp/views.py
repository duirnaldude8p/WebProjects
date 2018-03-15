from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .models import Cat
from .models import Cat_Comment
from .models import Comment
from .models import Account
from .models import Main
from .models import User

from .serializers import CatSerializer
from .serializers import CatCommentSerializer
from .serializers import CommentSerializer
from .serializers import AccountSerializer
from .serializers import MainSerializer
from .serializers import UserSerializer

from itertools import chain
# Create your views here.

def main(request):
	return render(request, "index.html", {})



class CommentGetData(generics.RetrieveAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def get(self, request):
		queryset = Comment.objects.all()
		serializer_class = CommentSerializer(queryset, many=True)
		
		return Response(serializer_class.data)


class CommentPostData(generics.CreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def post(self, request):
		serializer_class = CommentSerializer(data=request.data)
		if serializer_class.is_valid():
			Comment.objects.create(
				comment = request.POST.get('comment'),
			)
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class CatCommentGetData(generics.RetrieveUpdateAPIView):
	queryset = Cat_Comment.objects.all()
	serializer_class = CatCommentSerializer
	#print("cat comment queryset %s"%queryset)

	def get(self, request):
		queryset = Cat_Comment.objects.all()
		serializer_class = CatCommentSerializer(queryset, many=True)
		
		return Response(serializer_class.data)


class CatCommentPostData(generics.CreateAPIView):
	queryset = Cat_Comment.objects.all()
	serializer_class = CatCommentSerializer
	#print("cat comment queryset %s"%queryset)

	def post(self, request):
		serializer_class = CatCommentSerializer(data=request.data)
		if serializer_class.is_valid():
			Cat_Comment.objects.create(
				cat_comment = request.POST.get('cat_comment'),
			)
			serializer_class.save()

			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class UserGetData(generics.RetrieveUpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	#print("cat comment queryset %s"%queryset)

	def get(self, request):
		queryset = User.objects.all()
		serializer_class = UserSerializer(queryset, many=True)
		
		return Response(serializer_class.data)


class UserPostData(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	#print("cat comment queryset %s"%queryset)

	def post(self, request):
		serializer_class = UserSerializer(data=request.data)
		if serializer_class.is_valid():
			User.objects.create(
				username = request.POST.get('username'),
				password = request.POST.get('password')
			)
			serializer_class.save()

			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

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
		serializer_class = CatSerializer(data=request.data)
		if serializer_class.is_valid():
			#CatSerializer.create(self, request.data)
			cat_comment_data = request.POST.get('cat_comments')
			cat = Cat.objects.create(
            							user = request.POST.get('user_id'),
            							cat_name = request.POST.get('cat_name'),
            	       					breed = request.POST.get('breed'),
            							story = request.POST.get('story'),
            							cat_pic = request.POST.get('cat_pic'),
            							cat_comments = cat_comment_data
									)

			for cat_comment in cat_comment_data:
				cat_comment, created = Cat_Comment.objects.get_or_create(cat_comment=cat_comment['cat_comment'])
				cat.cat_comments.add(cat_comment)

			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountData(generics.RetrieveUpdateAPIView):
	queryset = Account.objects.all()
	serializer_class = AccountSerializer

	def get(self, request):
		queryset = Account.objects.all()
		serializer_class = AccountSerializer(queryset, many=True)
		
		return Response(serializer_class.data)

	def post(self, request):
		serializer_class = AccountSerializer(data=request.data)
		if serializer_class.is_valid():
			Account.objects.create(
				name = request.POST.get('name'),
				profile_pic = request.POST.get('profile_pic'),
				cats = request.POST.get('cats'),
				cat_comments = request.POST.get('cat_comments'),
				comments = request.POST.get('comments'),
				user = request.POST.get('user'),
				account_id = request.POST.get('account_id')
			)
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class MainData(generics.RetrieveUpdateAPIView):
	queryset = Main.objects.all()
	serializer_class = MainSerializer


	def get(self, request):
		queryset = Main.objects.all()
		serializer_class = MainSerializer(queryset, many=True)
		
		return Response(serializer_class.data)

	def post(self, request):
		# serializer_class = MainSerializer(data=request.data)
		# if serializer_class.is_valid():
		# 	# Main.objects.create(
		# 	# 	home_pic = request.POST.get('home_pic'),
		# 	# 	cats = request.POST.get('cats'),
		# 	# 	cat_comments = request.POST.get('cat_comments'),
		# 	# 	comments = request.POST.get('comments'),
		# 	# 	accounts = request.POST.get('accounts')
		# 	# )
		# 	serializer_class.save()
		# 	return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		# return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer_class.data)

# Create your views here.

