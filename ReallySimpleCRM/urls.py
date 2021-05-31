from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from contacts.views import LandingPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('contacts/', include('contacts.urls', namespace="contacts"))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
