from django.db import models

class User(models.Model):
    # canine = models.ForeignKey(Canine, 
    # on_delete=models.CASCADE, 
    # related_name='users',
    # default= models.CharField(max_length=100, default='canine_id'))
    # feline = models.ForeignKey(Feline, 
    # on_delete=models.CASCADE, 
    # related_name='users',
    # default= models.CharField(max_length=100, default= 'feline_id')
    userName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.userName

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
    related_name='canines', default=1, null = True, blank = True) 
    shelter = models.ForeignKey(Shelter, 
    on_delete=models.CASCADE, 
    related_name='canines', 
    null=True)
    dogName = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    photo_url = models.CharField(max_length=200, default = "no dice!")
    # dog_id = models.CharField(max_length=100)

    def __str__(self):
        return self.dogName

class Feline(models.Model):
    user = models.ForeignKey(User, 
    on_delete=models.CASCADE, 
    related_name='felines', default=1, null = True, blank = True)
    shelter = models.ForeignKey(Shelter, 
    on_delete=models.CASCADE, 
    related_name='felines', 
    null=True)
    catName = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    photo_url = models.CharField(max_length=200, default = "no dice!")
    # cat_id = models.CharField(max_length=100)

    def __str__(self):
        return self.catName