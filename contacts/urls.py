from django.urls import path
from .views import contact_list, contact_detail, contact_create

app_name = "contacts"

urlpatterns = [
  path('', contact_list),
  path('create/', contact_create),
  path('<int:pk>/', contact_detail),
]
