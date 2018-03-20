from rest_framework import serializers

import json

from .models import Cat
from .models import Account
from .models import Main
from .models import User


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
		cat_comment = validated_data['cat_comments']
		cat_comment = json.dumps([])
		cat_comment = json.loads(cat_comment)
		cat = Cat.objects.all()
		queryset = Cat.objects.all()
		if section == 'new':
			print("in new")
			cat = Cat.objects.create(
             							cat_name = validated_data['cat_name'],
             	       					breed = validated_data['breed'],
             							story = validated_data['story'],
             							cat_pic = validated_data['cat_pic'],
             							section = 'new',
             							category = 'cat',
             							cat_user = validated_data['cat_user'],
             							cat_comments = cat_comment
			 						)
			return cat
				
		if section == 'update comments':				
			print("in update")
			recieved_id = validated_data['get_id']
			for obj in cat.iterator():
				if obj.id == int(recieved_id):
					print("update id match")
					catComments = obj.cat_comments
					catComments = catComments.replace("'", '\"')
					catComments = json.loads(catComments)
					new_cat_comment = json.dumps({"cat_comment": validated_data['cat_comments'] })
					new_cat_comment = json.loads(new_cat_comment)
					catComments.append(new_cat_comment)
					Cat.objects.filter(pk=recieved_id).update(cat_comments=catComments)
					break
			
			return cat
		
		return cat
	

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account

		fields = ('__all__')

	def create(self, validated_data):
		print("in cat create serializer")
		section = validated_data['section']
		acc_comment = json.dumps([])
		acc_comment = json.loads(acc_comment)
		acc_cat_comment = json.dumps([])
		acc_cat_comment = json.loads(acc_cat_comment)
		acc_cat = json.dumps([])
		acc_cat = json.loads(acc_cat)
		account = Account.objects.all()
		if section == 'new':
			account = Account.objects.create(
											account_user = validated_data['account_user'],
											account_name = validated_data['account_name'],
											profile_pic = validated_data['profile_pic'],
											cats = acc_cat,
											cat_comments = acc_cat_comment,
											comments = acc_comment,
											section = 'new',
             								category = 'cat'
        								)
			return account
			
		if section == 'update comments':
			print("in update")
			recieved_id = validated_data['get_id']
			for obj in account.iterator():
				if obj.id == int(recieved_id):
					print("each obj: %s"%obj)
				# 	# add comments
					comments = obj.comments
					comments = comments.replace("'", '\"')
					comments = json.loads(comments)
					new_comment = json.dumps({"comment": validated_data['comments']})
					new_comment = json.loads(new_comment)
					comments.append(new_comment)
					Account.objects.filter(pk=recieved_id).update(comments=comments)
				# 	# add cats
					break
			return account

		if section == 'update cat comments':
			print("in update")
			recieved_id = validated_data['get_id']
			for obj in account.iterator():
				if obj.id == int(recieved_id):
					print("each obj: %s"%obj)
			# 		# add cat_comments	
					ac_catcomments = obj.cat_comments
					ac_catcomments = ac_catcomments.replace("'", '\"')
					ac_catcomments = json.loads(ac_catcomments)
					ac_new_catcomment = json.dumps({"cat_comment": validated_data['cat_comments']})
					ac_new_catcomment = json.loads(ac_new_catcomment)
					ac_catcomments.append(ac_new_catcomment)
					Account.objects.filter(pk=recieved_id).update(cat_comments=ac_catcomments)

					break
			return account
		if section == 'update cats':
			print("in update")
			recieved_id = validated_data['get_id']
			for obj in account.iterator():
				if obj.id == int(recieved_id):
					print("each obj: %s"%obj)
					# 	# add cats
					ac_cats = obj.cats
					ac_cats = ac_cats.replace("'", '\"')
					ac_cats = json.loads(ac_cats)
					ac_new_cat = json.dumps({"cat": validated_data['cats']})
					ac_new_cat = json.loads(ac_new_cat)
					ac_cats.append(ac_new_cat)
					Account.objects.filter(pk=recieved_id).update(cats=ac_cats)

					break
			return account
            	
		return account

		
class MainSerializer(serializers.ModelSerializer):
	class Meta:
		model = Main

		fields = ('__all__')

	def create(self, validated_data):
		print("in cat create serializer")
		section = validated_data['section']
		mn_comment = json.dumps([])
		mn_comment = json.loads(mn_comment)
		mn_cat_comment = json.dumps([])
		mn_cat_comment = json.loads(mn_cat_comment)
		mn_cat = json.dumps([])
		mn_cat = json.loads(mn_cat)
		mn_account = json.dumps([])
		mn_account = json.loads(mn_account)
		main = Main.objects.all()
		if section == 'new':
			main = Main.objects.create(
											accounts = mn_account,
											home_pic = validated_data['home_pic'],
											cats = mn_cat,
											cat_comments = mn_cat_comment,
											comments = mn_comment,
											section = 'new',
             								category = 'cat'
        								)
			return main
			
		if section == 'update comments':
			print("in update")
			recieved_id = validated_data['get_id']
			for obj in main.iterator():
				if obj.id == int(recieved_id):
					print("each obj: %s"%obj)
				 	# add comment
					comments = obj.comments
					comments = comments.replace("'", '\"')
					comments = json.loads(comments)
					new_comment = json.dumps({"comment": validated_data['comments']})
					new_comment = json.loads(new_comment)
					comments.append(new_comment)
					Main.objects.filter(pk=recieved_id).update(comments=comments)

					break
			return main

		if section == 'update cat comments':
			print("in update")
			recieved_id = validated_data['get_id']
			for obj in main.iterator():
				if obj.id == int(recieved_id):
					print("each obj: %s"%obj)
			 		# add cat_comment
					ac_catcomments = obj.cat_comments
					ac_catcomments = ac_catcomments.replace("'", '\"')
					ac_catcomments = json.loads(ac_catcomments)
					ac_new_catcomment = json.dumps({"cat_comment": validated_data['cat_comments']})
					ac_new_catcomment = json.loads(ac_new_catcomment)
					ac_catcomments.append(ac_new_catcomment)
					Main.objects.filter(pk=recieved_id).update(cat_comments=ac_catcomments)

					break
			return main
		if section == 'update cats':
			print("in update")
			recieved_id = validated_data['get_id']
			for obj in main.iterator():
				if obj.id == int(recieved_id):
					print("each obj: %s"%obj)
				 	# add cat
					ac_cats = obj.cats
					ac_cats = ac_cats.replace("'", '\"')
					ac_cats = json.loads(ac_cats)
					ac_new_cat = json.dumps({"cat": validated_data['cats']})
					ac_new_cat = json.loads(ac_new_cat)
					ac_cats.append(ac_new_cat)
					Main.objects.filter(pk=recieved_id).update(cats=ac_cats)

					break
			return main

		if section == 'update accounts':
			print("in update")
			recieved_id = validated_data['get_id']
			for obj in main.iterator():
				if obj.id == int(recieved_id):
					print("each obj: %s"%obj)
				 	# add account
					mn_accounts = obj.accounts
					mn_accounts = mn_accounts.replace("'", '\"')
					mn_accounts = json.loads(mn_accounts)
					mn_new_account = json.dumps({"account": validated_data['accounts']})
					mn_new_account = json.loads(mn_new_account)
					mn_accounts.append(mn_new_account)
					Main.objects.filter(pk=recieved_id).update(cats=mn_accounts)

					break
			return main
            	

		return main

	
