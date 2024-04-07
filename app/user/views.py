from rest_framework import generics ,authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import (UserSerializer,
     AuthtokenSerializer                         
)
class createUserView(generics.CreateAPIView):
    serializer_class=UserSerializer



class createTokenView(ObtainAuthToken):
    serializer_class=AuthtokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication = [authentication.TokenAuthentication]
    permission_class = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
