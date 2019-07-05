from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
