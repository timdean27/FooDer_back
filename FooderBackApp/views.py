from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Gfood

# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import generics
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .serializers import GfoodSerializer
# Create your views here.


class GfoodList(generics.ListCreateAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer

class GfoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer