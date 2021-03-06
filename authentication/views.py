from django.contrib import auth
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView
# Create your views here.
from authentication.serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.authtoken.models import Token


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # if serializer.user is not None:
            #     token = Token.objects.create(user=serializer.user)
            #     send_mail('helo lall', f'{token.key}', 'd3dkof@gmail.com', [serializer.user.email], fail_silently=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            serializer = UserSerializer(user)

            data = {'user': serializer.data}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
