from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contact, User
from .forms import ContactForm, ContactModelForm, CustomUserCreationForm
import xlwt
import openpyxl
import pandas as pd
from sqlalchemy import create_engine


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

def export_contacts_xls(request):
  response = HttpResponse(content_type='application/ms-excel')
  response['Content-Disposition'] = 'attachment; filename="users.xls"'

  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet("Contact List")

  row_num = 0
  font_style = xlwt.XFStyle()
  font_style.font.bold = True

  columns = ['first_name', 'last_name', 'email', 'address_1', 'address_2', 'city', 'state', 'zipcode', 'profile_photo', 'user']

  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)

  font_style = xlwt.XFStyle()

  rows = Contact.objects.filter(user=request.user).values_list('first_name', 'last_name', 'email', 'address_1', 'address_2', 'city', 'state', 'zipcode', 'profile_photo', 'user')

  for row in rows:
    row_num += 1
    for col_num in range(len(row)):
      ws.write(row_num, col_num, row[col_num], font_style)

  wb.save(response)
  return response

def import_contacts_xls(request):
  if request.method == "post" and request.FILES['excel_file']:
    excel_file = request.FILES['excel_file']

    wb = openpyxl.load_workbook(excel_file)
    active_sheet = wb.active
    print(active_sheet)

    return render(request, 'contacts:contact-list', {'xls_data': active_sheet})

# step 1 - create a view to handle uploading xls file
# step 2 - load xls file with openpyxl
# step 3 - seed db with xls data
# step 4 - render updated contact list on html
