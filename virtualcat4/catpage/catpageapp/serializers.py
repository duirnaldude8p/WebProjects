from rest_framework import serializers

import json

from .models import Cat
from .models import Account
from .models import Main
from .models import CurrentAccount
from .models import CatUniqueId
from random import randint

import os
from django.core.files.storage import default_storage
from pathlib import Path

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
					new_cat_comment = json.dumps({'cat_comment': {'comm': validated_data['cat_comments'], 'name': validated_data['name'], 'picture': validated_data['picture']}})
					new_cat_comment = json.loads(new_cat_comment)
					catComments.append(new_cat_comment)
					cat = Cat.objects.filter(pk=recieved_id).update(cat_comments=catComments)
					break
			
			return cat
		
		return cat
	

class AccountSerializer(serializers.ModelSerializer):
	
	def create(self, validated_data):
		print("in account create serializer")
		section = validated_data['section']
		account = Account.objects.all()
		#print("image: %s"%validated_data['profile_pic'])
		def profile_image_path(acc_id, filename):
			return os.path.join('catpageapp\static\pics\profile', acc_id, filename)
		def profile_image_path2(acc_id):
			return os.path.join('catpageapp\static\pics\profile', acc_id, "")
		if section == 'new':
			print("in new account")
			account = Account.objects.create(
											account_name = validated_data['account_name'],
											profile_pic = validated_data['profile_pic'],
											username = validated_data['username'],
											password = validated_data['password'],
											section = 'new',
             								category = 'account'
        								)
			#Account.save()
			return account
			
		if section == 'update picture':
				print("in update")
				recieved_id = validated_data['get_id']
				for obj in account.iterator():
					if obj.id == int(recieved_id):
						filename = validated_data['profile_pic'].name
						acc_id = validated_data['get_id']
						filepath = profile_image_path(acc_id, filename)
						filepath2 = profile_image_path2(acc_id)
						p = Path(filepath2)
						my_pths = [pth for pth in p.iterdir() 
									if pth.suffix == '.jpeg' or pth.suffix == '.jpg' or pth.suffix == '.png']
						#print("my_pths: %s"%my_pths)
						file_count = 0
						for path in my_pths:
							next_filename = os.path.basename(path)
							file_count = file_count + 1
							print("next name %s my name %s"%(next_filename, filename))
							if next_filename == filename:
								break
						print("file found: %s"%file_count==len(my_pths))
						print("file count: %s"%file_count)
						print("my pth length: %s"%len(my_pths))
						# Account.objects.filter(pk=recieved_id).update(profile_pic=filepath)
						# file_obj = validated_data['profile_pic']
						# with default_storage.open(filepath, 'wb+') as destination:
						# 	for chunk in file_obj.chunks():
						# 		destination.write(chunk)
						# break	
				return account
	
		#Account.save()    	
		return account

	class Meta:
		model = Account

		fields = ('__all__')


class CurrentAccountSerializer(serializers.ModelSerializer):

	class Meta:
		model = CurrentAccount
		#print("hello curr acc ser meta")
		fields = (
					'id', 
					'username', 
					'password', 
					'profile_pic', 
					'account_name', 
					'get_id', 
					'current_id', 
					'is_verified', 
					'section',
					'category',
					'filename'
				)

	def create(self, validated_data, *args, **kwargs):
		print("in current account create serializer")
		section = validated_data['section']
		current_account = CurrentAccount.objects.all()
		account = Account.objects.all()
		myaccount = None
		myid = 1
		def profile_image_path(acc_id, filename):
			return os.path.join('catpageapp\static\pics\profile', acc_id, filename)
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
											section = 'new',
             								category = 'current account',
             								current_id = myid,
             								is_verified = "true"
             								)
				return current_account
			
			if section == 'logout':
				current_account = CurrentAccount.objects.all().delete()
				return current_account	

			if section == 'update picture':
				print("in update")
				recieved_id = validated_data['get_id']
				for obj in current_account.iterator():
					if obj.id == int(recieved_id):
						filename = validated_data['profile_pic'].name
						acc_id = validated_data['current_id']
						filepath = profile_image_path(acc_id, filename)
						CurrentAccount.objects.filter(pk=recieved_id).update(profile_pic=filepath)
						file_obj = validated_data['profile_pic']
						with default_storage.open(filepath, 'wb+') as destination:
							for chunk in file_obj.chunks():
								destination.write(chunk)
						break	
				return current_account		
			
			return current_account
	



		
class MainSerializer(serializers.ModelSerializer):
	class Meta:
		model = Main

		fields = ('__all__')

	def create(self, validated_data):
		print("in main create serializer")
		section = validated_data['section']
		mn_comment = json.dumps([])
		mn_comment = json.loads(mn_comment)
		mn_cat_id = json.dumps([])
		mn_cat_id = json.loads(mn_cat_id)
		main = Main.objects.all()
		cat = Cat.objects.all()
		cat_unique_id = CatUniqueId.objects.all()
		if not main:
			if section == 'new':
				main = Main.objects.create(
											home_pic = validated_data['home_pic'],
											comments = mn_comment,
											section = 'new',
             								category = 'main',
             								my_cat_id = mn_cat_id
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

						my_cat_ids = obj.my_cat_id
						my_cat_ids = my_cat_ids.replace("'", '\"')
						print("before cats: %s"%my_cat_ids)
						my_cat_ids = json.loads(my_cat_ids)
						print("after cats: %s"%my_cat_ids)
						cat_story = validated_data['story']
						print("before cat story: %s"%cat_story)
						cat_story = json.dumps(cat_story)
						cat_story = json.loads(cat_story)
						print("cat story: %s"%cat_story)
						Cat.objects.create(
             							cat_name = validated_data['cat_name'],
             	       					breed = validated_data['breed'],
             							story = cat_story,
             							cat_pic = validated_data['cat_pic'],
             							section = 'update cats',
             							category = 'cat',
             							cat_unique_id = my_unique_cat_id,
             							cat_comments = "[]"
			 						)
		
						
						my_new_cat_id = Cat.objects.filter(cat_unique_id=my_unique_cat_id)[0].id
						#my_new_cats2 = [my_new_cat for my_new_cat in my_new_cats]
						#print("my new cat %s"%my_new_cats2)
						print("my new cat ids before %s"%my_cat_ids)
						print("my new id before %s"%my_new_cat_id)
						my_cat_ids.append(my_new_cat_id)
						print("my new cat %s"%my_cat_ids)
						Main.objects.filter(pk=recieved_id).update(my_cat_id=my_cat_ids)
						break
				return main
			return main


	
