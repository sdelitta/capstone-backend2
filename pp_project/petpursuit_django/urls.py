from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petpursuit.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]