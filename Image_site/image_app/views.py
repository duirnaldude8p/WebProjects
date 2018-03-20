from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .models import Picture

from .serializers import PictureSerializer

# Create your views here.

def main(request):
	return render(request, 'basic.html')

class PictureGetData(generics.RetrieveAPIView):
	queryset = Picture.objects.all()
	serializer_class = PictureSerializer

	#print("cat queryset: %s"%queryset)
	
	def get(self, request):
		queryset = Picture.objects.all()
		serializer_class = PictureSerializer(queryset, many=True)
		
		return Response(serializer_class.data)

class PicturePostData(generics.CreateAPIView):
	queryset = Picture.objects.all()
	serializer_class = PictureSerializer

	def post(self, request):
		serializer_class = PictureSerializer(data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
