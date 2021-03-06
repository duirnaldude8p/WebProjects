from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

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

# Create your views here.

registered = False

# def login_page(request):
# 	return render(request,'login_app/login.html')

# def profile_page(request):
# 	return render(request,'login_app/profile.html')

# def register_page(request):
# 	return render(request,'login_app/register.html')

def home_page(request):
	return render(request,'login_app/index.html')


# @method_decorator(login_required, name="post")
# class ProfileData(APIView):
# 	renderer_classes = [TemplateHTMLRenderer]
# 	template_name = 'login_app/profile.html'
# 	queryset = UserProfileInfo.objects.all() 
# 	serializer_class = RegisterSerializer 
# 	user = User
# 	# prof = UserProfileInfo.objects.get(user=request.user)
# 	# username = prof.username    

# 	def get(self, request):
# 		prof = UserProfileInfo.objects.get(user=request.user)
# 		username = prof.user.username 
# 		profile_pic = prof.profile_pic
# 		print("username %s"%username)
# 		return Response({'profile_pic':profile_pic, 'username':username}) 
    
# 	def post(self, request):
# 		prof = UserProfileInfo.objects.get(user=request.user)
# 		username = prof.user.username 
# 		profile_pic = prof.profile_pic
# 		recieved_pic = request.POST.get('profile_pic')
# 		return Response({'profile_pic':profile_pic, 'username':username}) 


# @method_decorator(login_required, name="get")	
# class Profile_Data(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'login_app/profile.html'
#     queryset = UserProfileInfo.objects.all() 
#     serializer_class = RegisterSerializer 
#     # permission_classes = (permissions.IsAuthenticated,)
    
#     def get(self, request):
#         prof = UserProfileInfo.objects.get(user=request.user)
#         username = prof.user.username 
#         profile_pic = prof.profile_pic
#         profile_form = UserProfileInfoForm()
#         # print("username %s"%username)
#         return Response({'profile_pic':profile_pic, 'profile_form': profile_form, 'username':username}) 
    

#     def update(self, request, *args, **kwargs):

#         prof = UserProfileInfo.objects.get(user=request.user)
#         username = prof.user.username 
#         profile_pic = prof.profile_pic

#         serializer_class = RegisterSerializer(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()

#             # print("valid user_form %s"%user_form)
#             return Response({'serializer': serializer_class, 'profile_pic':profile_pic, 'username':username}, status=status.HTTP_201_CREATED)
#         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

# class AccountPostData(generics.CreateAPIView):
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
    def post(self, request):
        profile = UserProfileInfo.objects.get(user=request.user)
        username = profile.user.username 
        profile_pic = profile.profile_pic

        
        if 'profile_pic' in request.FILES:
            # print('found it')
            profile.profile_pic = request.FILES['profile_pic']

        profile.save()
        
        return Response({'profile_pic':profile.profile_pic, 'username':username})

       

        serializer_class = ProfileSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'data': serializer_class.data, 'profile_pic':profile.profile_pic, 'username':username}, status=status.HTTP_201_CREATED)
        print("errors: %s"%serializer_class._errors)
        return Response(serializer_class._errors, status=status.HTTP_400_BAD_REQUEST)




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

    

    


