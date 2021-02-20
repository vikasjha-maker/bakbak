
from django.contrib.auth import get_user_model
from .models import Insta
from rest_framework.authtoken.models import Token
from rest_framework import serializers 
from django.contrib.auth import authenticate
from rest_framework import exceptions

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=( 'email', 'password')
        
        def create (self,validated_data):
            user = User.create_user(validated_data['email'], validated_data['password'])

            return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ( 'email', 'password')
        #fields='__all__'
        
    def validate(self, values):
        user = authenticate(email=values['email'], password = values['password'])
        if user is not None:
            return user
        else:
            raise serializers.ValidationError("invalid login")

            return user






class Instaserializer(serializers.ModelSerializer):
    class Meta:
        model = Insta
        fields = ('id', 'user_name', 'date', 'desc', 'image')
        


