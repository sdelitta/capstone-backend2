from django.urls import path
from . import views

urlpatterns = [
    path('', views.state_list, name='state_list'),
    path('users/', views.user_list, name='user_list'),
    path('shelters/', views.shelter_list, name='shelter_list'),
    path('canines/', views.canine_list, name='canine_list'),
    path('felines/', views.feline_list, name='feline_list'),
    path('canines/<int:pk>', views.canine_detail, name='canine_detail'),
    path('felines/<int:pk>', views.feline_detail, name='feline_detail'),
    path('states/<int:pk>', views.state_detail, name='state_detail'),
    path('shelters/<int:pk>', views.shelter_detail, name='shelter_detail'),
    path('users/<int:pk>', views.user_detail, name='user_detail'),
    path('users/new', views.user_create, name='user_create'),
    path('users/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete', views.user_delete, name='user_delete'),
]