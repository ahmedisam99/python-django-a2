from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet 

from .models import Book
from .serializers import BookSerializer

# Create your views here.
def get_all_books(req):
    return HttpResponse('This is the books page')


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
