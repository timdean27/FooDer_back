from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('Gfoods/', views.GfoodList.as_view(), name='gfood_list'),
    path('Gfoods/<int:pk>', views.GfoodDetail.as_view(), name='gfood_detail'),

]