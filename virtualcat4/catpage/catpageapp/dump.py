print("each obj: %s"%obj)
				 		# add cat
						ac_cats = obj.cats
						ac_cats = ac_cats.replace("'", '\"')
						ac_cats = json.loads(ac_cats)
						ac_cats = json.loads(ac_cats.decode('utf-8'))
						#my_cat_comments = json.dumps([])
						my_cat_comments = json.loads("[]")
						ac_new_cat = {	
										"cat": {	
											"cat_name": validated_data['cat_name'], 
											"breed": validated_data['breed'], 
											"cat_pic": validated_data['cat_pic'], 
											"story": validated_data['story'], 
											"cat_comments": "[]"
										}
									}
						# print("type %s"%type(ac_new_cat))
						# ac_new_cat = dict(ac_new_cat)
						json.dumps(ac_new_cat)
						# print("typ2 %s"%type(ac_new_cat))
						# ac_new_cat = str(ac_new_cat)
						# ac_new_cat = eval(ac_new_cat)
						# print("str: %s"%ac_new_cat)
						print("type %s"%type(ac_new_cat))
						ac_new_cat = json.loads(ac_new_cat.decode('utf-8'))
						ac_cats.append(ac_new_cat)
						Main.objects.filter(pk=recieved_id).update(cats=ac_cats)
									#unique_ids.append(my_unique_cat_id)
									# 	unique_ids = CatUniqueId.objects.cat_id
						# unique_ids = unique_ids.replace("'", '\"')
						# unique_ids = json.loads(unique_ids)
