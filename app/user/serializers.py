from django.contrib.auth  import (get_user_model,authenticate)
from rest_framework import serializers
from django.utils.translation import gettext as _
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['email','password','name']
        extra_kwargs={'password':{
            'write_only':True,'min_length':5
        }}
        
    def create(self,validate_data):
        return get_user_model().objects.createUser(**validate_data)
    
class AuthtokenSerializer(serializers.Serializer):
         email=serializers.EmailField()
         password=serializers.CharField(trim_whitespace=False)

         def validate(self,attrs):
              email=attrs.get('Email')
              password=attrs.get('password')
              user=authenticate(
                   request=self.context.get('request'),
                   username=email,
                   password=password
              )
              if not user:
                   msg=_('unable to authenticate with provided credentials')
                   raise serializers.ValidationError(msg,code='authorization')
              
              attrs['user']=user
              return user

                 
