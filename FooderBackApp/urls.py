from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('gfoods/', views.GfoodList.as_view(), name='gfood_list'),
    path('gfoods/<int:pk>', views.GfoodDetail.as_view(), name='gfood_detail'),
    
    path('gfoods_protected/', views.GfoodListProtected.as_view(), name='gfood_detail'),
]