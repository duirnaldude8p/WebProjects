
class PostUserData(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def post(self, request):
		serializer_class = UserSerializer(data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)