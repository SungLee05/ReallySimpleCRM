from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact, User
from .forms import ContactForm, ContactModelForm

def landing_page(request):
  return render(request, "landing_page.html")

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
      form.save()
      return redirect('/contacts')

  context = {
    "form": ContactModelForm()
  }

  return render(request, "contact_create.html", context )

def contact_update(request, pk):
  contact = Contact.objects.get(id=pk)
  form = ContactModelForm(instance=contact)
  if request.method == "POST":
      form = ContactModelForm(request.POST, instance=contact)
      if form.is_valid():
          form.save()
          return redirect('/contacts')
  context = {
    "contact": contact,
    "form": form
  }
  return render(request, "contact_update.html", context)

def contact_delete(request, pk):
  contact = Contact.objects.get(id=pk)
  contact.delete()
  return redirect('/contacts')
