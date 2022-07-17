from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework import generics , permissions
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .serializers import GfoodSerializer

from .models import Gfood
# Create your views here.


class GfoodList(generics.ListCreateAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer

class GfoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer

class GfoodListProtected(generics.ListCreateAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer
    
    permission_classes = [permissions.IsAuthenticated]

class GfoodUpdateProtected(generics.UpdateAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer
    
    permission_classes = [permissions.IsAuthenticated]