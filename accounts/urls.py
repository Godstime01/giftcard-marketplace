from django.urls import path, include
from . import views

urlpatterns = [
    path("register/<str:code>/", views.UserCreationView.as_view(), name='register'),
    path("register/", views.UserCreationView.as_view(), name='register'),
    path("login/", views.CustomLoginView.as_view(), name='login' ),
    path('wallet/', views.WalletView.as_view(), name='wallet'),
    path('', include('django.contrib.auth.urls'))
]