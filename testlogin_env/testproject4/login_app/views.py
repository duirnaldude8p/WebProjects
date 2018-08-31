from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view

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

# # Create your views here.

registered = False
new_dispatch = None


def home_page(request):
	return render(request,'login_app/index.html')


@method_decorator(login_required, name="get") 
class Profile_Data(APIView):
    # print("HELLO PROFILE POST")
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login_app/profile.html'
    queryset = UserProfileInfo.objects.all() 
    serializer_class = RegisterSerializer 
    
    @api_view(['GET', 'POST', 'PUT'])
    def dispatch(self, request, *args, **kwargs):
        profile = UserProfileInfo.objects.get(user=request.user)
        current_id = profile.id
   
        if request.method == 'POST':
            return self.put(request._request, current_id, *args, **kwargs)

        return super().dispatch(request._request, *args, **kwargs)
    
    def get(self, request):
        prof = UserProfileInfo.objects.get(user=request.user)
        username = prof.user.username 
        profile_pic = prof.profile_pic
        profile_form = UserProfileInfoForm()
        current_id = prof.id
        print("get method user id %s"%prof.id)
        return Response({'profile_pic':profile_pic, 'profile_form': profile_form, 'username':username, "current_id" :current_id}) 
    
    
    print("in postdata")
    def post(self, request):
        print("HELLO POST")
        profile = UserProfileInfo.objects.get(user=request.user)
        username = profile.user.username 
        profile_pic = profile.profile_pic
        current_id = profile.id
        
        if 'profile_pic' in request.FILES:
            # print('found it')
            profile.profile_pic = request.FILES['profile_pic']

        profile.save()
        
        return Response({'profile_pic':profile.profile_pic, 'username':username, "current_id" :current_id})

       

        serializer_class = RegisterSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'data': serializer_class.data, 'profile_pic':profile.profile_pic, 'username':username, "current_id" :current_id}, status=status.HTTP_201_CREATED)
        print("errors: %s"%serializer_class._errors)
        return Response(serializer_class._errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        print("IN PUT METHOD")
        profile = UserProfileInfo.objects.get(user=request.user)
        username = profile.user.username 
        profile_pic = profile.profile_pic
        current_id = profile.id
        
        if 'profile_pic' in request.FILES:
            # print('found it')
            profile.profile_pic = request.FILES['profile_pic']

        profile.save()
        
        return Response({'profile_pic':profile.profile_pic, 'username':username, "current_id" :current_id})

        profile = self.get_object(pk)
        serializer = RegisterSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

# class Profile_Put(APIView):

    

    



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
            print(user_form.errors, profile_form.errors)
            return Response({'user_form':user_form, 'profile_form': profile_form, 'registered': registered})

        serializer_class = RegisterSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            print("valid user_form %s"%user_form)
            return Response({'serializer': serializer_class, 'user_form':user_form, 'profile_form': profile_form, 'registered': registered}, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    

    




# # Create your views here.
