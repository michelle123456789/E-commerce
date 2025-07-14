from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import User,Listing
from .forms import ListingForm


def index(request):
    listings=Listing.objects.all()
    return render(request, "auctions/index.html",{
        "listings":listings
    })

def newListing(request):
    submitted = False
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)  # don’t save yet
            listing.user = request.user        # assign the currently logged-in user
            form.save()
            return HttpResponseRedirect(reverse("newListing") + "?submitted=True")
    #did not click on create button -> either first clicked to add a new listing or redirected after adding a listing
    else:
        form = ListingForm()
        #test if form submitted
        if "submitted" in request.GET:
            submitted = True
    return render(request,"auctions/newListing.html",{
        'form':form,
        'submitted':submitted
    })

def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, "auctions/listing.html",{
        "listing": listing
    })

@login_required
def watchlist(request):
    watchlist = request.user.watchlist.all()
    return render(request, "auctions/watchlist.html",{
        "watchlist": watchlist
    })

@login_required
def toggle_watchlist(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    if listing in request.user.watchlist.all():
        request.user.watchlist.remove(listing)
    else:
        request.user.watchlist.add(listing)

    return redirect("listing", listing_id=listing.id)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
