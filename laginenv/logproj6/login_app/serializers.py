from rest_framework import serializers

from .models import UserProfileInfo
from django.contrib.auth.models import User



class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfileInfo
		fields = ('__all__')

	def create(self, validated_data):
		print("create user profile: %s"%validated_data.get('username'))

		 # Get info from "both" forms
        # It appears as one form to the user on the .html page
		user_form = UserForm(data=validated_data)
		profile_form = UserProfileInfoForm(data=validated_data)
		profile = UserProfileInfoForm()

		# Check to see both forms are valid
		if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
			user = user_form.save()

            # Hash the password
			user.set_password(user.password)

            # Update with Hashed password
			user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
			profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
			profile.user = user

            # Check if they provided a profile picture
			if 'profile_pic' in request.FILES:
				print('found it')
                # If yes, then grab it from the POST form reply
				profile.profile_pic = request.FILES['profile_pic']

            # Now save model
			profile.save()	
		else:
			# One of the forms was invalid if this else gets called.
			print(user_form.errors,profile_form.errors)


		

		return profile
		