from urllib import response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
# Create your views here.
class RegisterApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            # Handle invalid data case here, e.g., return a response with errors
            return Response(serializer.errors, status=400)
        
        serializer.save()
        return Response(serializer.data)
    
class LoginApiView(APIView):
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()

        if not user:
            raise APIException('Invalid credentials')
        
        if not user.check_password(request.data['password']):
            raise APIException('invalid credentials')
        
        serializer = UserSerializer(user)

        return Response(serializer.data)
