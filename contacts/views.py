from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Contact, User
from .forms import ContactForm, ContactModelForm

class LandingPageView(generic.TemplateView):
  template_name = "landing_page.html"

class ContactListView(generic.ListView):
  template_name = "contact_list.html"
  queryset = Contact.objects.all()
  context_object_name = 'contacts'

class ContactDetailView(generic.DetailView):
  template_name = "contact_detail.html"
  queryset = Contact.objects.all()
  context_object_name = 'contact'

class ContactCreateView(generic.CreateView):
  template_name = "contact_create.html"
  form_class = ContactModelForm
  def get_success_url(self):
    return reverse("contacts:contact-list")

class ContactUpdateView(generic.UpdateView):
  template_name = "contact_update.html"
  queryset = Contact.objects.all()
  form_class = ContactModelForm
  def get_success_url(self):
    return reverse("contacts:contact-list")

class ContactDeleteView(generic.DeleteView):
  template_name = "contact_delete.html"
  queryset = Contact.objects.all()
  form_class = ContactModelForm
  def get_success_url(self):
    return reverse("contacts:contact-list")
