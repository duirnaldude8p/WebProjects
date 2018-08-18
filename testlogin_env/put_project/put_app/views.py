from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .models import PutModel

class Put_Data(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'put_app.html'
	queryset = PutModel.objects.all() 
	put_model = PutModel.objects.all() 
    # serializer_class = RegisterSerializer 
    # permission_classes = (permissions.IsAuthenticated,)
	
    
    def get(self, request):
		query = request.GET.get("firstname")
		if query:
			put_model = PutModel.objects.filter(firstname = self.id).order_by('id')

		my_put = PutModel.objects.all()[:1].get()
		firstname = my_put.firstname 
		lastname = my_put.lastname 

		return Response({'firstname':firstname, 'lastname': lastname}) 
    
    
    # print("in postdata")
	def post(self, request):
		query = request.GET.get("firstname")
		if query:
			put_model = PutModel.objects.filter(firstname = self.id).order_by('id')

		my_put = PutModel.objects.all()[:1].get()
		my_put.firstname = request.POST.get("firstname")
		my_put.lastname = request.POST.get("lastname")
		firstname = my_put.firstname 
		lastname = my_put.lastname 

		return Response({'firstname':firstname, 'lastname': lastname}) 
	
        
		

       

        # serializer_class = ProfileSerializer(data=request.data)
        # if serializer_class.is_valid():
        #     serializer_class.save()
        #     return Response({'data': serializer_class.data, 'profile_pic':profile.profile_pic, 'username':username}, status=status.HTTP_201_CREATED)
        # print("errors: %s"%serializer_class._errors)
        # return Response(serializer_class._errors, status=status.HTTP_400_BAD_REQUEST)


