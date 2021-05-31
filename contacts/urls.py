from django.urls import path
from .views import contact_list, contact_detail, contact_create, contact_update, contact_delete

app_name = "contacts"

urlpatterns = [
  path('', contact_list, name="contact-list"),
  path('create/', contact_create, name="contact-create"),
  path('<int:pk>/', contact_detail, name="contact-detail"),
  path('<int:pk>/update/', contact_update, name="contact-update"),
  path('<int:pk>/delete/', contact_delete, name="contact-delete"),
]
