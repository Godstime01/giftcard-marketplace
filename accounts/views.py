import uuid
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import AccountCreationForm, LoginForm
from .models import Referral, UserModel

class CustomLoginView(UserPassesTestMixin, LoginView):
    form_class = LoginForm
    login_url = '/dashboard'

    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        # Redirect authenticated users to the home page
        messages.info(self.request, "You're already logged in..")
        return redirect('/dashboard')


def get_referer(code):
    return UserModel.objects.get(referrer_id=code)


class UserCreationView(UserPassesTestMixin, FormView):
    form_class = AccountCreationForm
    success_url = '/'
    template_name = 'registration/register.html'
    code = None # refferal code 
    request = None

    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        # Redirect authenticated users to the home page
        return redirect('/dashboard')

    def get(self, request, *args: str, **kwargs):
        print(request.path)
        self.request = request
        self.code = request.path.split("/")[-2]
        print(self.code)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form, *args, **kwargs):
        self.code = self.kwargs.get('code')
        # self.code = kwargs.get('code')
        print(f"CODE {self.code}")
        # TODO: check if user with refferal code exist 
        if self.code:
            referer = get_referer(self.code)
            user = form.save(commit=False)
            user.referred_by = referer
            user.save()
            # referer is the user that person signup with their code
            # referred_user is user registering now

            Referral(referring_user=referer, referred_user=user).save()
        else:
            # create user account
            form.save()
            
        # print(referer.username)    
        # user = form.save(commit=False)
        # user.referred_by = referer
        # user.save()
        # if self.code:
        #     Referral(user = user, code_used=self.code).save()

            # print('referral saved')
        return super().form_valid(form)

class WalletView(TemplateView):
    template_name = 'wallet.html'
    