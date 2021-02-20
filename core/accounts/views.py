from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LoginSerializer,Instaserializer,RegisterSerializer
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import Insta
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


class RegisterView(APIView):
    def get(self,request):
        query_set = User.objects.all()
        serializer = RegisterSerializer(query_set,many=True)

        return Response(serializer.data,status=200)
        
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid()
        if serializer.validated_data is not None and serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            token,created = Token.objects.get_or_create(user = user)
            
            return Response({"token":token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    def post(self, request):
        logout(request)
        
        return Response(status=204)


class InstaModelView(APIView):
    def get(self, request):
        query_set = Insta.objects.all()
        serializer = Instaserializer(query_set, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = Instaserializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)

        return Response(serializer.errors, status = 400)


class InstaDetailView(APIView):
    """
    Retrieve, update or delete a Insta instance.
    """
    def get_object(self, pk):
        try:
            return Insta.objects.get(pk=pk)
        except Insta.DoesNotExist:
            raise Response( {"error": "Given id object is not found. "}, status=404)

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = Instaserializer(instance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = Instaserializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=204)