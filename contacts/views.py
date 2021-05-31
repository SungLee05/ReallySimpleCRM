from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contact, User
from .forms import ContactForm, ContactModelForm, CustomUserCreationForm


class SignupView(generic.CreateView):
  template_name = "registration/signup.html"
  form_class = CustomUserCreationForm
  def get_success_url(self):
    return reverse("login")

class LandingPageView(generic.TemplateView):
  template_name = "landing_page.html"

class ContactListView(LoginRequiredMixin, generic.ListView):
  template_name = "contact_list.html"
  context_object_name = 'contacts'

  def get_queryset(self):
    queryset = Contact.objects.all()
    if self.request.user.is_authenticated:
      queryset = queryset.filter(user=self.request.user)
    return queryset

class ContactDetailView(LoginRequiredMixin, generic.DetailView):
  template_name = "contact_detail.html"
  context_object_name = 'contact'

  def get_queryset(self):
    queryset = Contact.objects.all()
    if self.request.user.is_authenticated:
      queryset = queryset.filter(user=self.request.user)
    return queryset

class ContactCreateView(LoginRequiredMixin, generic.CreateView):
  template_name = "contact_create.html"
  form_class = ContactModelForm

  def get_success_url(self):
    return reverse("contacts:contact-list")

  def form_valid(self, form):
    contact = form.save(commit=False)
    contact.user = self.request.user
    contact.save()
    return super(ContactCreateView, self).form_valid(form)

class ContactUpdateView(LoginRequiredMixin, generic.UpdateView):
  template_name = "contact_update.html"
  form_class = ContactModelForm

  def get_queryset(self):
    queryset = Contact.objects.all()
    if self.request.user.is_authenticated:
      queryset = queryset.filter(user=self.request.user)
    return queryset

  def get_success_url(self):
    return reverse("contacts:contact-list")

class ContactDeleteView(LoginRequiredMixin, generic.DeleteView):
  template_name = "contact_delete.html"
  form_class = ContactModelForm

  def get_queryset(self):
    queryset = Contact.objects.all()
    if self.request.user.is_authenticated:
      queryset = queryset.filter(user=self.request.user)
    return queryset

  def get_success_url(self):
    return reverse("contacts:contact-list")
