from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.StateList.as_view(), name='StateList'),
    path('users/', views.UserList.as_view(), name='UserList'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='UserDetail'),
    path('shelters/', views.ShelterList.as_view(), name='ShelterList'),
    path('canines/', views.CanineList.as_view(), name='CanineList'),
    path('felines/', views.FelineList.as_view(), name='FelineList'),
    path('canines/<int:pk>', views.CanineDetail.as_view(), name='CanineDetail'),
    path('felines/<int:pk>', views.FelineDetail.as_view(), name='FelineDetail'),
    path('states/<int:pk>', views.StateDetail.as_view(), name='StateDetail'),
    path('shelters/<int:pk>', views.ShelterDetail.as_view(), name='ShelterDetail'),
    # path('users/new', views.UserCreate.as_view(), name='UserCreate'),
    # path('users/<int:pk>/edit', views.UserEdit.as_view(), name='UserEdit'),
    # path('users/<int:pk>/delete', views.UserDelete.as_view(), name='UserDelete'),
]