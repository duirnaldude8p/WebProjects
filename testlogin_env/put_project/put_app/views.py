from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

# from .models import Put
from .models import UserProfileInfo

from .serializers import RegisterSerializer
from .serializers import ProfileSerializer
from .forms import UserForm
from .forms import UserProfileInfoForm


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# class Put_Data(APIView):
# 	renderer_classes = [TemplateHTMLRenderer]
# 	template_name = 'put_app.html'
# 	queryset = Put.objects.all() 
#     # serializer_class = RegisterSerializer 
#     # permission_classes = (permissions.IsAuthenticated,)
    
# 	def get(self, request):
# 		put_model = Put.objects.get(user=request.user)
#         # username = prof.user.username 
# 		name = put_model.my_name
# 		return Response({'name':name}) 
    
    
#     # print("in postdata")
# 	def post(self, request):
# 		put_model = Put.objects.get(user=request.user)
# 		# username = profile.user.username 
# 		# profile_pic = profile.profile_pic
# 		put_model.my_name = request.POST.get('putname')
# 		name = put_model.my_name
# 		put_model.save()


        
		# return Response({'name':name}) 

registered = False

@method_decorator(login_required, name="get") 
class Profile_Data(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'login_app/profile.html'
	queryset = UserProfileInfo.objects.all() 
	serializer_class = RegisterSerializer 
    # permission_classes = (permissions.IsAuthenticated,)
    
	def get(self, request):
		prof = UserProfileInfo.objects.get(user=request.user)
		username = prof.user.username 
		profile_pic = prof.profile_pic
		profile_form = UserProfileInfoForm()
        # print("username %s"%username)
		return Response({'profile_pic':profile_pic, 'profile_form': profile_form, 'username':username}) 
    
    
    # print("in postdata")
    # def post(self, request):
    #     profile = UserProfileInfo.objects.get(user=request.user)
    #     username = profile.user.username 
    #     profile_pic = profile.profile_pic

        
    #     if 'profile_pic' in request.FILES:
    #         # print('found it')
    #         profile.profile_pic = request.FILES['profile_pic']

    #     profile.save()
    # return Response({'profile_pic':profile.profile_pic, 'username':username})

	def put(self, request, pk, format=None):
		prof = UserProfileInfo.objects.get(user=request.user)
		username = prof.user.username 
		profile_pic = prof.profile_pic
		profile_form = UserProfileInfoForm()

		reg = self.get_object(pk)
		serializer = RegisterSerializer(reg, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'data': serializer_class.data, 'profile_pic':profile.profile_pic, 'username':username}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

       

        # serializer_class = ProfileSerializer(data=request.data)
        # if serializer_class.is_valid():
        #     serializer_class.save()
        #     return Response({'data': serializer_class.data, 'profile_pic':profile.profile_pic, 'username':username}, status=status.HTTP_201_CREATED)
        # print("errors: %s"%serializer_class._errors)
        # return Response(serializer_class._errors, status=status.HTTP_400_BAD_REQUEST)




class Login_Data(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login_app/login.html'
    queryset = UserProfileInfo.objects.all()
    serializer_class = RegisterSerializer

    def get(self, request):
        user = User
        # print("In Login!")
        return Response({'url':'login'}) 

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:  
            if user.is_active:
                login(request, user)
                # print("Login successfull!")
                return  HttpResponseRedirect(reverse('profile'))
            else:
                return Response({'resp_message':'Inactive account'})
        else:
            return Response({'resp_message':'incorrect login details provided'})



class Register_Data(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login_app/register.html'
    queryset = UserProfileInfo.objects.all()
    serializer_class = RegisterSerializer
    
    
    def get(self, request):
        
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        queryset = UserProfileInfo.objects.all()
      
        serializer_class = RegisterSerializer(queryset, many=True)
        return Response({'serializer': serializer_class, 'user_form':user_form, 'profile_form': profile_form, 'registered': registered})


    def post(self, request):
        global registered
        registered = False

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

        
            profile.user = user

            if 'profile_pic' in request.FILES:
                # print('found it')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
            return Response({'user_form':user_form, 'profile_form': profile_form, 'registered': registered})

        else:
            print(user_form.errors,profile_form.errors)
            return Response({'user_form':user_form, 'profile_form': profile_form, 'registered': registered})

        serializer_class = RegisterSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            print("valid user_form %s"%user_form)
            return Response({'serializer': serializer_class, 'user_form':user_form, 'profile_form': profile_form, 'registered': registered}, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)