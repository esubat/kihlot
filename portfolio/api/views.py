from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny

from .serializers import UserRegistrationSerializer, UserDetailSerializer


class RegisterView(APIView):

    permission_classes = [AllowAny]
    def post(self, request , *args , **kwargs):

        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            login_url = reverse('api_login')
            return Response(
                {"message" : f"{user.username} successfully resgistered",
                 "login_url": login_url
                 },
                   status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny,]
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username = username , password = password)
        
        if user is not None:
            login(request, user)
            serializer =UserDetailSerializer(user)

            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
       
       
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(
            {"message": "Successfully logged out"},
            status=status.HTTP_200_OK)


class UserDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request,username, *args, **kwargs):
        user = get_object_or_404(User, username = username)
        serializer = UserDetailSerializer(user)

        return Response(serializer.data , status = status.HTTP_200_OK)
    
