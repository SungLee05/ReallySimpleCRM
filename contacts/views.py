from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


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

