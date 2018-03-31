from rest_framework import serializers

import json

from .models import Cat
from .models import Account
from .models import Main
from .models import CurrentAccount
from .models import CatUniqueId
from random import randint

class CatSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cat

		fields = ('__all__')
	
	def create(self, validated_data):
		print("in cat create serializer")
		section = validated_data['section']
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
	
	def create(self, validated_data):
		print("in account create serializer")
		section = validated_data['section']
		acc_comment = json.dumps([])
		acc_comment = json.loads(acc_comment)
		acc_cat_comment = json.dumps([])
		acc_cat_comment = json.loads(acc_cat_comment)
		acc_cat = json.dumps([])
		acc_cat = json.loads(acc_cat)
		account = Account.objects.all()
		print("image: %s"%validated_data['profile_pic'])
		if section == 'new':
			print("in new account")
			account = Account.objects.create(
											account_name = validated_data['account_name'],
											profile_pic = validated_data['profile_pic'],
											username = validated_data['username'],
											password = validated_data['password'],
											cats = acc_cat,
											cat_comments = acc_cat_comment,
											comments = acc_comment,
											section = 'new',
             								category = 'account'
        								)
			#Account.save()
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
			#Account.save()
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
			#Account.save()
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
			#Account.save()
			return account
		#Account.save()    	
		return account

	class Meta:
		model = Account

		fields = ('__all__')


class CurrentAccountSerializer(serializers.ModelSerializer):
	
	def create(self, validated_data):
		print("in current account create serializer")
		section = validated_data['section']
		current_account = CurrentAccount.objects.all()
		account = Account.objects.all()
		myaccount = None
		myid = 1
		if not current_account:
			if section == 'login':
				myusr = validated_data['username']
				mypwd = validated_data['password']
				for obj in account.iterator():
					if obj.username == myusr and obj.password == mypwd:
						myaccount = Account.objects.filter(pk=obj.id)
						myid = obj.id
						break
				

				if myaccount:	
					current_account = CurrentAccount.objects.create(
											account_name = myaccount[0].account_name,
											profile_pic = myaccount[0].profile_pic,
											username = myaccount[0].username,
											password = myaccount[0].password,
											cats = myaccount[0].cats,
											cat_comments = myaccount[0].cat_comments,
											comments = myaccount[0].comments,
											section = 'new',
             								category = 'current account',
             								current_id = myid,
             								is_verified = "true"
             								)
				return current_account
			return current_account	
		else: 
			if section == 'login':
				myusr = validated_data['username']
				mypwd = validated_data['password']
				for obj in account.iterator():
					if obj.username == myusr and obj.password == mypwd:
						myaccount = Account.objects.filter(pk=obj.id)
						myid = obj.id
						break
				

				if myaccount:
					CurrentAccount.objects.all().delete()	
					current_account = CurrentAccount.objects.create(
											account_name = myaccount[0].account_name,
											profile_pic = myaccount[0].profile_pic,
											username = myaccount[0].username,
											password = myaccount[0].password,
											cats = myaccount[0].cats,
											cat_comments = myaccount[0].cat_comments,
											comments = myaccount[0].comments,
											section = 'new',
             								category = 'current account',
             								current_id = myid,
             								is_verified = "true"
             								)
				return current_account
			if section == 'update comments':
				print("in update")
				recieved_id = validated_data['get_id']
				for obj in current_account.iterator():
					if obj.id == int(recieved_id):
						print("each obj: %s"%obj)
						comments = obj.comments
						comments = comments.replace("'", '\"')
						comments = json.loads(comments)
						new_comment = json.dumps({"comment": validated_data['comments']})
						new_comment = json.loads(new_comment)
						comments.append(new_comment)
						CurrentAccount.objects.filter(pk=recieved_id).update(comments=comments)
						break
			
				return current_account

			if section == 'update cat comments':
				print("in update")
				recieved_id = validated_data['get_id']
				for obj in current_account.iterator():
					if obj.id == int(recieved_id):
						print("each obj: %s"%obj)
						ac_catcomments = obj.cat_comments
						ac_catcomments = ac_catcomments.replace("'", '\"')
						ac_catcomments = json.loads(ac_catcomments)
						ac_new_catcomment = json.dumps({"cat_comment": validated_data['cat_comments']})
						ac_new_catcomment = json.loads(ac_new_catcomment)
						ac_catcomments.append(ac_new_catcomment)
						CurrentAccount.objects.filter(pk=recieved_id).update(cat_comments=ac_catcomments)
						break

				return current_account
			if section == 'update cats':
				recieved_id = validated_data['get_id']
				for obj in current_account.iterator():
					if obj.id == int(recieved_id):
						print("each obj: %s"%obj)
						# 	# add cats
						ac_cats = obj.cats
						ac_cats = ac_cats.replace("'", '\"')
						ac_cats = json.loads(ac_cats)
						ac_new_cat = json.dumps({"cat": validated_data['cats']})
						ac_new_cat = json.loads(ac_new_cat)
						ac_cats.append(ac_new_cat)
						CurrentAccount.objects.filter(pk=recieved_id).update(cats=ac_cats)
						break
	
				return current_account
  
			return current_account
	class Meta:
		model = CurrentAccount

		fields = ('__all__')


	

		
class MainSerializer(serializers.ModelSerializer):
	class Meta:
		model = Main

		fields = ('__all__')

	def create(self, validated_data):
		print("in main create serializer")
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
		cat = Cat.objects.all()
		cat_unique_id = CatUniqueId.objects.all()
		if not main:
			if section == 'new':
				main = Main.objects.create(
											accounts = mn_account,
											home_pic = validated_data['home_pic'],
											cats = mn_cat,
											cat_comments = mn_cat_comment,
											comments = mn_comment,
											section = 'new',
             								category = 'main'
        								)
				return main
			return main	
		else:
			if section == 'update comments':
				print("in comment update")
				recieved_id = validated_data['get_id']
				print("my id %s"%validated_data['get_id'])
				for obj in main.iterator():
					if obj.id == int(recieved_id):

						print("hello obj: %s"%obj)
				 		# add comment
						comments = obj.comments
						comments = comments.replace("'", '\"')
						comments = json.loads(comments)
						new_comment = json.dumps({"comment": {"comm": validated_data['comments'], "name": validated_data['name'], "picture": validated_data['picture']}})
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
				print("in cat update")
				recieved_id = validated_data['get_id']
				print("my cat id: %s"%validated_data['get_id'])
				def random_with_N_digits(n):
					range_start = 10**(n-1)
					range_end = (10**n)-1
					return randint(range_start, range_end)
				for obj in Main.objects.all():
					if obj.id == int(recieved_id):
						numbers = range(1, 10)
						isfound = False
						while not isfound:
							randnum = random_with_N_digits(10)
							my_unique_cat_id = 0
							my_count = 0
							if cat_unique_id:
								for cid in cat_unique_id.iterator():
									if int(cid.cat_id) == randnum:
										break
									else:
										my_count = my_count + 1
								if my_count == cat_unique_id.count():
									my_unique_cat_id = str(randnum)
									CatUniqueId.objects.create(
										cat_id = my_unique_cat_id
									)
									isfound = True
								break
							else:
								my_unique_cat_id = str(randnum)
								CatUniqueId.objects.create(
									cat_id = my_unique_cat_id
								)
								break

						my_cats = obj.cats
						my_cats = my_cats.replace("'", '\"')
						my_cats = json.loads(my_cats)
						print("a after cats: %s"%my_cats)
						#cat_comment = json.dumps([])
						#cat_comment = json.loads(cat_comment)
						Cat.objects.create(
             							cat_name = validated_data['cat_name'],
             	       					breed = validated_data['breed'],
             							story = validated_data['story'],
             							cat_pic = validated_data['cat_pic'],
             							section = 'update cats',
             							category = 'cat',
             							cat_unique_id = my_unique_cat_id,
             							cat_comments = "[]"
			 						)
		
						
						my_new_cat = Cat.objects.filter(cat_unique_id=my_unique_cat_id).values()[0]
						print("my new cat %s"%my_new_cat)
						my_cats.append(my_new_cat)
						Main.objects.filter(pk=recieved_id).update(cats=my_cats)
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


	
