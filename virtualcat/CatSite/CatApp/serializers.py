from rest_framework import serializers

from .models import Cat
from .models import Cat_Comment
from .models import Comment
from .models import Account
from .models import Main
from .models import User

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('__all__')

class CatCommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cat_Comment
		fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('__all__')

class CatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cat

		fields = ('__all__')

		def create(validated_data):
			cat_comment_data = validated_data.pop('cat_comments')
			cat = Cat.objects.create(
        								cat_id = validated_data.cat_id,
            							user = validated_data['user'],
            							cat_name = validated_data['cat_name'],
            	       					breed = validated_data['breed'],
            							story = validated_data['story'],
            							cat_pic = validated_data['cat_pic'],
            							cat_comments = []
									)

			for cat_comment in cat_comment_data:
				cat_comment, created = Cat_Comment.objects.get_or_create(cat_comment=cat_comment['cat_comment'])
				cat.cat_comments.add(cat_comment)

			return cat


		def update(instance, validated_data):
			cat_comment_data = validated_data.pop('cat_comments')
			instance.cat_id = validated_data.cat_id
			instance.user = validated_data['user']
			instance.cat_name = validated_data['cat_name']
			instance.breed = validated_data['breed']
			instance.story = validated_data['story']
			instance.cat_pic = validated_data['cat_pic']

			for cat_comment in cat_comment_data:
				cat_comment, created = Cat_Comment.objects.get_or_create(cat_comment=cat_comment['cat_comment'])
				instance.cat_comments.add(cat_comment)

			return instance

		

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account

		fields = ('__all__')

		def create(alidated_data):
			cat_comment_data = validated_data.pop('cat_comments')
			comment_data = validated_data.pop('comments')
			cat_data = validated_data.pop('cats') 
			account = Cat.objects.create(
											account_id = validated_data.account_id,
											user = validated_data['user'],
											name = validated_data['name'],
											profile_pic = validated_data['profile_pic'],
											cats = [],
											cat_comments = [],
											comments = []
        								)

			for cat_comment in cat_comment_data:
				cat_comment, created = Cat_Comment.objects.get_or_create(cat_comment=cat_comment['cat_comment'])
				account.cat_comments.add(cat_comment)

			for comment in comment_data:
				comment, created = Comment.objects.get_or_create(comment=comment['comment'])
				account.comments.add(comment)

			for cat in cat_data:
				cat, created = Cat.objects.get_or_create(
															cat_id = cat.cat_id,
															user = cat['user'],
															cat_name = cat['cat_name'],
															breed = cat['breed'],
															story=cat['story'],
															cat_pic=cat['cat_pic'],
															cat_comments=cat['cat_comments']

														)

            	
			account.comments.add(cat)

			return account

		def update(instance, validated_data):
			cat_comment_data = validated_data.pop('cat_comments')
			comment_data = validated_data.pop('comments')
			cat_data = validated_data.pop('cats') 
			instance.account_id = validated_data['account_id']
			instance.user = validated_data['user']
			instance.name = validated_data['name']
			instance.profile_pic = validated_data['profile_pic']


			for cat_comment in cat_comment_data:
				cat_comment, created = Cat_Comment.objects.get_or_create(cat_comment=cat_comment['cat_comment'])
				instance.cat_comments.add(cat_comment)

			for comment in comment_data:
 				comment, created = Comment.objects.get_or_create(comment=comment['comment'])
 				instance.comments.add(comment)

			for cat in cat_data:
				cat, created = Cat.objects.get_or_create(
															cat_id = cat.cat_id,
            												user = cat['user'],
            												cat_name = cat['cat_name'],
            												breed = cat['breed'],
            												story = cat['story'],
            												cat_pic = cat['cat_pic'],
            												cat_comments = cat['cat_comments']
            											)

            	
				instance.comments.add(cat)

			return instance

	

class MainSerializer(serializers.ModelSerializer):
	class Meta:
		model = Main

		fields = ('__all__')

		# def create(self, validated_data):
		# 	cat_data = validated_data.pop('cats')
		# 	cat_comment_data = validated_data.pop('cat_comments')
		# 	comment_data = validated_data.pop('comments')
		# 	account_data = validated_data.pop('account')
		# 	main = Main.objects.create(
		# 									home_pic = validated_data['home_pic'],
		# 									cat = [],
		# 									cat_comments = [],
		# 									comments = [],
		# 									accounts = []
		# 								)

		# 	for cat in cat_data:
		# 		cat, created = Cat.objects.get_or_create(
		# 													cat_id = cat.cat_id,
  #           												user = cat['user'],
  #           												cat_name = cat['cat_name'],
  #           												breed = cat['breed'],
  #           												story = cat['story'],
  #           												cat_pic = cat['cat_pic'],
  #           												cat_comments = cat['cat_comments']
  #           											)

            	
		# 		main.comments.add(cat)

		# 	for cat_comment in cat_comment_data:
		# 		cat_comment, created = Cat_Comment.objects.get_or_create(cat_comment=cat_comment['cat_comment'])
		# 		main.cat_comments.add(cat_comment)

		# 	for comment in comment_data:
		# 		comment, created = Comment.objects.get_or_create(comment=comment['comment'])
		# 		main.comments.add(comment)

		# 	for account in account_data:
		# 		account, created = Account.objects.get_or_create(
		# 													account_id = account.account_id,
  #           												user = account['user'],
  #           												name = account['name'],
  #           												profile_pic = account['profile_pic'],
  #           												cats = account['cats'],
  #           												cat_comments = account['cat_comments']
  #           											)

            	
		# 		main.comments.add(account)


		# 	return main

		# def update(self, instance, validated_data):
		# 	cat_data = validated_data.pop('cats')
		# 	cat_comment_data = validated_data.pop('cat_comments')
		# 	comment_data = validated_data.pop('comments')
		# 	account_data = validated_data.pop('account')
		# 	instance.home_pic = validated_data['home_pic']



		# 	for cat in cat_data:
		# 		cat, created = Cat.objects.get_or_create(
		# 													cat_id = cat.cat_id,
  #           												user = cat['user'],
  #           												cat_name = cat['cat_name'],
  #           												breed = cat['breed'],
  #           												story = cat['story'],
  #           												cat_pic = cat['cat_pic'],
  #           												cat_comments = cat['cat_comments']
  #           											)

            	
		# 		instance.comments.add(cat)

		# 	for cat_comment in cat_comment_data:
		# 		cat_comment, created = Cat_Comment.objects.get_or_create(cat_comment=cat_comment['cat_comment'])
		# 		instance.cat_comments.add(cat_comment)

		# 	for comment in comment_data:
		# 		comment, created = Comment.objects.get_or_create(comment=comment['comment'])
		# 		instance.comments.add(comment)

		# 	for account in account_data:
		# 		account, created = Account.objects.get_or_create(
		# 													account_id = account.account_id,
  #           												user = account['user'],
  #           												name = account['name'],
  #           												profile_pic = account['profile_pic'],
  #           												cats = account['cats'],
  #           												cat_comments = account['cat_comments']
  #           											)

            	
		# 		instance.comments.add(account)


		# 	return instance

	

