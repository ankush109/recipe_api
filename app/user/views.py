from rest_framework import generics
from user.serializers import UserSerializer

class createUserView(generics.CreateAPIView):
    serializer_class=UserSerializer
