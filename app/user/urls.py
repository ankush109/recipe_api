# url mapings for the user
from django.urls import path 
from user import views

app_name='user'

urlpatterns=[
    path('create/',views.createUserView.as_view(),name='create'),
    path('token/',views.createTokenView.as_view(),name='token')
    
]