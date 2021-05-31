from django.contrib import admin
from django.urls import path, include
from contacts.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing-page'),
    path('contacts/', include('contacts.urls', namespace="contacts"))
]
