from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass
  #creating own User model (inheriting AbstractUser model) to have more flexibility to add customized fields as needed.

class Contact(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  email = models.EmailField(blank=True, null=True, max_length=254)
  address_1 = models.CharField(blank=True, null=True, max_length=20)
  address_2 = models.CharField(blank=True, null=True, max_length=20)
  city = models.CharField(blank=True, null=True, max_length=20)
  state = models.CharField(blank=True, null=True, max_length=20)
  zipcode = models.CharField(blank=True, null=True, max_length=5)
  profile_photo = models.ImageField(blank=True, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  #foreign key requires on_delete in case relational table is deleted. setting it to cascade to ensure contact list that is associated with a specific user is deleted if user profile no longer exist. can be set to null if contact list needs to exist regardless.

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

