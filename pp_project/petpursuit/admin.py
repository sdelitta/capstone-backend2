from django.contrib import admin
from .models import User, Canine, Feline, Shelter, State

class UserAdmin(admin.ModelAdmin):
    model = User

admin.site.register(User, UserAdmin)
admin.site.register(State)
admin.site.register(Shelter)
admin.site.register(Canine)
admin.site.register(Feline)
