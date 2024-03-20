from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.

class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return Response({'detail': 'login successful'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class Register(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'message': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)

class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out'}, status=status.HTTP_200_OK)

    
