
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('accounts.urls')),
    path("dashboard/", include('dashboard.urls')),

    path('', views.HomePageView.as_view(), name='index')
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)