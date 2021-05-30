from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact, User
from .forms import ContactForm, ContactModelForm


def contact_list(request):
  contacts = Contact.objects.all()
  context = {
    "contacts": contacts
  }
  return render(request, "contact_list.html", context )

def contact_detail(request, pk):
  contact = Contact.objects.get(id=pk)
  context = {
    "contact": contact
  }
  return render(request, "contact_detail.html", context )

def contact_create(request):
  form = ContactModelForm()

  if request.method == "POST":
    print('Receiving a post request')
    form = ContactModelForm(request.POST)
    if form.is_valid():
      print('The form is valid')
      print(form.cleaned_data)
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      email = form.cleaned_data['email']
      user = form.cleaned_data['user']
      Contact.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        user=user
      )
      print('contact has been created')
      return redirect('/contacts')

  context = {
    "form": ContactModelForm()
  }

  return render(request, "contact_create.html", context )

# def contact_create(request):
#   form = ContactForm()

#   if request.method == "POST":
#     print('Receiving a post request')
#     form = ContactModelForm(request.POST)
#     if form.is_valid():
#       print('The form is valid')
#       print(form.cleaned_data)
#       first_name = form.cleaned_data['first_name']
#       last_name = form.cleaned_data['last_name']
#       email = form.cleaned_data['email']
#       user = User.objects.first()
#       Contact.objects.create(
#         first_name=first_name,
#         last_name=last_name,
#         email=email,
#         user=user
#       )
#       print('contact has been created')
#       return redirect('/contacts')

#   context = {
#     "form": ContactForm()
#   }

#   return render(request, "contact_create.html", context )
