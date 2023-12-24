from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Library
from rest_framework import viewsets
from .serializers import LibrarySerializer

 
class LibraryViewSet(viewsets.ModelViewSet):   
  queryset = Library.objects.all().order_by('Publisher')
  serializer_class = LibrarySerializer
