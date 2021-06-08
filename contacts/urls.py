from django.urls import path
from .views import ContactListView, ContactDetailView, ContactCreateView, ContactUpdateView, ContactDeleteView, export_contacts_xls, import_contacts_xls

app_name = "contacts"

urlpatterns = [
  path('', ContactListView.as_view(), name="contact-list"),
  path('create/', ContactCreateView.as_view(), name="contact-create"),
  path('<int:pk>/', ContactDetailView.as_view(), name="contact-detail"),
  path('<int:pk>/update/', ContactUpdateView.as_view(), name="contact-update"),
  path('<int:pk>/delete/', ContactDeleteView.as_view(), name="contact-delete"),
  path('export/excel/', export_contacts_xls, name='contact-export'),
  path('import/excel/', import_contacts_xls, name='contact-import')
]
