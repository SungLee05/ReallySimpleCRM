from django import forms
from .models import Contact

class ContactModelForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = (
        'first_name',
        'last_name',
        'email',
        'address_1',
        'address_2',
        'city',
        'state',
        'zipcode',
        'profile_photo',
        'user'
    )



class ContactForm(forms.Form):
  first_name = forms.CharField(max_length=20)
  last_name = forms.CharField(max_length=20)
  email = forms.EmailField(required=False, max_length=254)
  address_1 = forms.CharField(required=False, max_length=20)
  address_2 = forms.CharField(required=False, max_length=20)
  city = forms.CharField(required=False, max_length=20)
  state = forms.CharField(required=False, max_length=20)
  zipcode = forms.IntegerField(required=False)
  profile_photo = forms.ImageField(required=False)
