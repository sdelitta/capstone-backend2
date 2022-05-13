from petpursuit import serializers
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # JavaScript Web Tokens
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token-create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
    path('blacklist/', views.UserLogout.as_view(), name='token-blacklist'),

    path('states/', views.StateList.as_view(), name='StateList'),
    path('states/<int:pk>', views.StateDetail.as_view(), name='StateDetail'),    
    path('shelters/', views.ShelterList.as_view(), name='ShelterList'),
    path('shelters/<int:pk>', views.ShelterDetail.as_view(), name='ShelterDetail'),
    path('canines/', views.CanineList.as_view(), name='CanineList'),
    path('felines/', views.FelineList.as_view(), name='FelineList'),
    path('canines/<int:pk>', views.CanineDetail.as_view(), name='CanineDetail'),
    path('felines/<int:pk>', views.FelineDetail.as_view(), name='FelineDetail'),
    
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/create', views.UserCreate.as_view(), name='user_create'),
    path('users/logout', views.UserLogout.as_view(), name='user_logout'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/<str:username>', views.UserDetailByUsername.as_view(), name='user_detail_by_username'),

    # path('users/<int:pk>/edit', views.user_edit.as_view(), name='user_edit')

    # path('users/create', views.UserCreate.as_view(), name='UserCreate'),
    # path('users/', views.UserList.as_view(), name='UserList'),
    # path('users/<int:pk>', views.UserDetail.as_view(), name='UserDetail'),
    # path('users/<int:pk>/edit', views.UserEdit.as_view(), name='UserEdit'),
    # path('users/<int:pk>/delete', views.UserDelete.as_view(), name='UserDelete'),
]