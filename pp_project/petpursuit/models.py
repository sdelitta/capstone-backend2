from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # canine = models.ForeignKey(Canine, 
    # on_delete=models.CASCADE, 
    # related_name='users',
    # default= models.CharField(max_length=100, default='canine_id'))
    # feline = models.ForeignKey(Feline, 
    # on_delete=models.CASCADE, 
    # related_name='users',
    # default= models.CharField(max_length=100, default= 'feline_id'))

    def __str__(self):
        return self.username

class State(models.Model):
    stateName = models.CharField(max_length=100)

    def __str__(self):
        return self.stateName

class Shelter(models.Model):
    state = models.ForeignKey(State, 
    on_delete=models.CASCADE, 
    related_name='shelters')
    shelterName = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.shelterName

class Canine(models.Model):
    user = models.ForeignKey(User, 
    on_delete=models.CASCADE, 
    related_name='canines', null = True, blank = True) 
    shelter = models.ForeignKey(Shelter, 
    on_delete=models.CASCADE, 
    related_name='canines', 
    null=True)
    dogName = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    photo_url = models.CharField(max_length=400, default = "no dice!")
    userCanine = models.ManyToManyField(User, through='UserCanines')

    def __str__(self):
        return self.dogName

class Feline(models.Model):
    user = models.ForeignKey(User, 
    on_delete=models.CASCADE, 
    related_name='felines', null = True, blank = True)
    shelter = models.ForeignKey(Shelter, 
    on_delete=models.CASCADE, 
    related_name='felines', 
    null=True)
    catName = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    photo_url = models.CharField(max_length=400, default = "no dice!")
    userFeline = models.ManyToManyField(User, through='UserFelines')

    def __str__(self):
        return self.catName

class UserCanines(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    canine = models.ForeignKey(Canine, on_delete=models.CASCADE)

class UserFelines(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feline = models.ForeignKey(Feline, on_delete=models.CASCADE)