from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework import generics , permissions ,viewsets
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .serializers import GfoodSerializer , UserSerializer

from .models import Gfood
from django.contrib.auth.models import User
# Create your views here.


class GfoodList(generics.ListAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer

class GfoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer


def mock_signup(request):
    return JsonResponse({'loggedIn':True, 'username': 'mock_user'})



class GfoodListProtected(generics.ListAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer
    
    permission_classes = [permissions.IsAuthenticated]

class GfoodCreateProtected(generics.CreateAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer
    
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        request.data['user_string'] = request.user.username
        return super().post(request, *args, **kwargs)
class GfoodUpdateProtected(generics.UpdateAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer
    
    permission_classes = [permissions.IsAdminUser]

class GfoodDeleteProtected(generics.DestroyAPIView):
    queryset = Gfood.objects.all()
    serializer_class = GfoodSerializer
    
    permission_classes = [permissions.IsAdminUser]

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()