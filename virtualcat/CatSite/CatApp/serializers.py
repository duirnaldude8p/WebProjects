from rest_framework import serializers

import json

from .models import Cat
from .models import Account
from .models import Main
from .models import User

# class CommentSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Comment
# 		fields = ('__all__')

# class CatCommentSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Cat_Comment
# 		fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('__all__')

class CatSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cat

		fields = ('__all__')
		print("in cat serializer")
	
	def create(self, validated_data):
		print("in cat create serializer")
		section = validated_data['section']
		print("section: %s"%section)
		cat_comment = validated_data['cat_comments']
		#cat_comment = str(cat_comment)
		cat_comment = json.dumps([{"cat_comment": cat_comment }])
		cat_comment = json.loads(cat_comment)
		#cat_comment = cat_comment.replace('\"', '"')
		print("in cat create serializers")
		cat = Cat.objects.all()
		if section == 'new':
			print("in new")
			cat = Cat.objects.create(
   	        							user = validated_data['user'],
             							cat_name = validated_data['cat_name'],
             	       					breed = validated_data['breed'],
             							story = validated_data['story'],
             							cat_pic = validated_data['cat_pic'],
             							section = 'new',
             							category = 'cat',
             							cat_comments = cat_comment
			 						)
			return cat
				
		if section == 'update':				
			print("in update")
			recieved_id = validated_data['get_id']
			print("recieved id: %s"%recieved_id)
			for obj in cat:
				print("cat ids: %s"%obj.id)
				print("cat ids: %s"%obj)
				# if obj.id == 5:
				# 	# print("update id match")
				# 	# catComments = obj.cat_comments
				# 	# print("recived info %s"%catComments)
				# 	# catComments = catComments.replace('\"', '"')
				# 	# print("recived info2 %s"%catComments)
				# 	# catComments = json.dumps(catComments)
				# 	# print("recived info3 %s"%catComments)
				# 	# catComments = json.loads(catComments)
				# 	# print("recived info4 %s"%catComments)
				# 	# #new_cat_comment = json.dumps({"cat_comment": validated_data['cat_comments'] })
				# 	# #new_cat_comment = json.loads(new_cat_comment)
				# 	# #catComments.append({"cat_comment": validated_data['cat_comments'] })
				# 	# obj.cat_comments = catComments
				# 	# break
					
			 	
			return cat

		return cat

	



		

		

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

	

