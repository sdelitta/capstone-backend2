from django.contrib import admin
from .models import User, Canine, Feline, Shelter, State

admin.site.register(User)
admin.site.register(State)
admin.site.register(Shelter)
admin.site.register(Canine)
admin.site.register(Feline)
