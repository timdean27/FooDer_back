from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [

    path('gfoods/', views.GfoodList.as_view(), name='gfood_list'),
    path('gfoods/<int:pk>', views.GfoodDetail.as_view(), name='gfood_detail'),
    
    path('mock_signup', views.mock_signup),
   
    path('api/', include(router.urls)),


    path('gfoods_view_protected/', views.GfoodListProtected.as_view(), name='gfood_detail'),
    path('gfoods_create_protected/', views.GfoodCreateProtected.as_view(), name='gfood_detail'),
    path('gfoods_update_protected/<int:pk>', views.GfoodUpdateProtected.as_view(), name='gfood_detail'),
    path('gfoods_delete_protected/<int:pk>', views.GfoodDeleteProtected.as_view(), name='gfood_detail'),
]