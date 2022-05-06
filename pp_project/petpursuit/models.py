from django.db import models

class State(models.Model):
    stateName = models.CharField(max_length=100)

    def __str__(self):
        return self.stateName

class Shelter(models.Model):
    state = models.ForeignKey(State, 
    on_delete=models.CASCADE, 
    related_name='shelters')
    shelterName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    website = models.TextField()

    def __str__(self):
        return self.shelterName

class Canine(models.Model):
    shelter = models.ForeignKey(Shelter, 
    on_delete=models.CASCADE, 
    related_name='canines')
    dogName = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.TextField()
    location = models.TextField()

    def __str__(self):
        return self.dogName

class Feline(models.Model):
    shelter = models.ForeignKey(Shelter, 
    on_delete=models.CASCADE, 
    related_name='felines')
    catName = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.TextField()
    location = models.TextField()

    def __str__(self):
        return self.catName

class User(models.Model):
    userName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.TextField()

    def __str__(self):
        return self.userName