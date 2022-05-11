from django.shortcuts import render, redirect
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, StateSerializer, ShelterSerializer, CanineSerializer, FelineSerializer, UserCaninesSerializer, UserFelinesSerializer
from .models import State, Shelter, User, Canine, Feline, UserCanines, UserFelines

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response(users)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                print(json)
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailByUsername(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class ShelterList(generics.ListCreateAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class ShelterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class CanineList(generics.ListCreateAPIView):
    queryset = Canine.objects.all()
    serializer_class = CanineSerializer

class CanineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Canine.objects.all()
    serializer_class = CanineSerializer

class FelineList(generics.ListCreateAPIView):
    queryset = Feline.objects.all()
    serializer_class = FelineSerializer

class FelineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feline.objects.all()
    serializer_class = FelineSerializer

class UserCaninesList(generics.ListCreateAPIView):
    queryset = UserCanines.objects.all()
    serializer_class = UserCaninesSerializer

class UserCaninesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCanines.objects.all()
    serializer_class = UserCaninesSerializer

class UserFelinesList(generics.ListCreateAPIView):
    queryset = UserFelines.objects.all()
    serializer_class = UserFelinesSerializer

class UserFelinesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserFelines.objects.all()
    serializer_class = UserFelinesSerializer

# class UserViewSet(viewsets.ViewSet):




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