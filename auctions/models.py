from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    #no additional fields added yet
    pass

class Listing(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    starting_bid = models.IntegerField()
    url_picture = models.CharField(max_length=80,default="None")
    category = models.CharField(max_length=20,default="Other")

#class Bids(models.Model):
#bid = models.IntegerField()
#user = 

#class Comments(models.Model):
# user =
# comment = models.TextField()
