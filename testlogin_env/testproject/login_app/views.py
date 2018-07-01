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
from .forms import UserForm
from .forms import UserProfileInfoForm
# Create your views here.

registered = False

def login_page(request):
	return render(request,'login_app/login.html')

def profile_page(request):
	return render(request,'login_app/profile.html')

# def register_page(request):
# 	return render(request,'login_app/register.html')

class Register_Data(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login_app/register.html'
    queryset = UserProfileInfo.objects.all()
    serializer_class = RegisterSerializer
    
    
    def get(self, request):

        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        queryset = UserProfileInfo.objects.all()
        # formdict = {
        #     'user_form': user_form ,
        #     'profile_form': profile_form ,
        #     'registered': registered
        # }
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
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)

        serializer_class = RegisterSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'serializer': serializer_class, 'user_form':user_form, 'profile_form': profile_form, 'registered': registered}, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    

    

