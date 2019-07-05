from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet #The view class to be inhireted from the view

from .serializers import UserSerializer

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
