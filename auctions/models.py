from django.contrib.auth.models import AbstractUser
from django.db import models
from commerce import settings


class User(AbstractUser):
    #no additional fields added yet
    watchlist = models.ManyToManyField("Listing", blank=True, related_name="watched_by") #a user cna have many listings in their watchlist and a listing can be in many users's watchlists

    '''user.watchlist.all()           # Listings the user is watching
       listing.watched_by.all()       # Users who are watching this listing'''

class Listing(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    starting_bid = models.IntegerField()
    url_picture = models.CharField(max_length=1000,blank=True)
    category = models.CharField(max_length=20,blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # refers to your custom User model
        on_delete=models.CASCADE,  # if user is deleted, delete their listings
        related_name="listings",    # access via user.listings.all()
        default = 1 #sets the admin user
    )

#class Bids(models.Model):
#bid = models.IntegerField()
#user = 

#class Comments(models.Model):
# user =
# comment = models.TextField()
