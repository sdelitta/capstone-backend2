from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.state_list.as_view(), name='state_list'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('shelters/', views.shelter_list.as_view(), name='shelter_list'),
    path('canines/', views.canine_list.as_view(), name='canine_list'),
    path('felines/', views.feline_list.as_view(), name='feline_list'),
    path('canines/<int:pk>', views.canine_detail.as_view(), name='canine_detail'),
    path('felines/<int:pk>', views.feline_detail.as_view(), name='feline_detail'),
    path('states/<int:pk>', views.state_detail.as_view(), name='state_detail'),
    path('shelters/<int:pk>', views.shelter_detail.as_view(), name='shelter_detail'),
    path('users/new', views.user_create.as_view(), name='user_create'),
    path('users/<int:pk>/edit', views.user_edit.as_view(), name='user_edit'),
    path('users/<int:pk>/delete', views.user_delete.as_view(), name='user_delete'),
]