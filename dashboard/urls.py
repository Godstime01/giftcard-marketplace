from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.DashboardUser.as_view(), name='users'),
    path('agents/', views.DashboardAllAgent.as_view(), name='agents'),
    path('cards/', views.DashboardAllCard.as_view(), name='cards'),
    path('transactions/', views.DashboardAllTransaction.as_view(), name='transactions'),
    path('referrals/', views.DashboardReferral.as_view(), name='referrals'),
    path('wallet/', views.DashboardReferral.as_view(), name='wallet'),
    path('', views.DashboardOverview.as_view(), name='overview'),
    
]