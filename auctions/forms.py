from django import forms 
from django.forms import ModelForm
from .models import Listing

#create a Listing form
class ListingForm(ModelForm):
    #allows to define things in form
    class Meta:
        model=Listing
        fields = ('title','description','starting_bid','url_picture','category')
        # Optional: add Bootstrap classes & a textarea
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 4}
            ),
            "starting_bid": forms.NumberInput(attrs={"class": "form-control"}),
            "url_picture": forms.URLInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
        }