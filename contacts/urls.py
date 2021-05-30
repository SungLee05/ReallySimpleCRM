from django.urls import path
from .views import contact_list, contact_detail

app_name = "contacts"

urlpatterns = [
  path('', contact_list),
  path('<pk>/', contact_detail)
]
