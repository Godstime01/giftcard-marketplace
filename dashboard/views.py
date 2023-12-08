from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import UserModel, Referral


class DashboardOverview(LoginRequiredMixin, TemplateView):
    template_name = 'overview.html'


class DashboardUser(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = 'users.html'
    context_object_name = 'users'

    def get_queryset(self):
        query = UserModel.objects.filter(is_agent=False).filter(is_superuser=False)
        return query

class DashboardAllAgent(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = 'agents.html'
    context_object_name = 'agents'

    def get_queryset(self):
        query = UserModel.objects.filter(is_agent=True)
        return query

class DashboardAllCard(LoginRequiredMixin, TemplateView):
    template_name = 'cards.html'


class DashboardAllTransaction(LoginRequiredMixin, TemplateView):
    template_name = 'transactions.html'


class DashboardReferral(LoginRequiredMixin, TemplateView):
    template_name = 'referral.html'