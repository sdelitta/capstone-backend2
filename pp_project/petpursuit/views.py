from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import UserSerializer
from .forms import StateForm, ShelterForm, CanineForm, FelineForm, UserForm
from .models import State, Shelter, User, Canine, Feline

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# def state_list(request):
#     states = State.objects.all()
#     return render(request, 'petpursuit/state_list.html', {'states': states})

# def shelter_list(request):
#     shelters = Shelter.objects.all()
#     return render(request, 'petpursuit/shelter_list.html', {'shelters': shelters})

# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'petpursuit/user_list.html', {'users': users})

# def canine_list(request):
#     canines = Canine.objects.all()
#     return render(request, 'petpursuit/canine_list.html', {'canines': canines})

# def feline_list(request):
#     felines = Feline.objects.all()
#     return render(request, 'petpursuit/feline_list.html', {'felines': felines})


# def canine_detail(request, pk):
#     canine = Canine.objects.get(id=pk)
#     return render(request, 'petpursuit/canine_detail.html', {'canine': canine})

# def feline_detail(request, pk):
#     feline = Feline.objects.get(id=pk)
#     return render(request, 'petpursuit/feline_detail.html', {'feline': feline})

# def shelter_detail(request, pk):
#     shelter = Shelter.objects.get(id=pk)
#     return render(request, 'petpursuit/shelter_detail.html', {'shelter': shelter})

# def state_detail(request, pk):
#     state = State.objects.get(id=pk)
#     return render(request, 'petpursuit/state_detail.html', {'state': state})

# def user_detail(request, pk):
#     user = User.objects.get(id=pk)
#     return render(request, 'petpursuit/user_detail.html', {'user': user})


# def user_create(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('user_detail', pk=user.pk)
#     else:
#         form = UserForm()
#     return render(request, 'petpursuit/user_form.html', {'form': form})

# def user_edit(request, pk):
#     user = User.objects.get(pk=pk)
#     if request.method == "POST":
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             user = form.save()
#             return redirect('user_detail', pk=user.pk)
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'petpursuit/user_form.html', {'form': form})

# def user_delete(request, pk):
#     User.objects.get(id=pk).delete()
#     return redirect('user_list')