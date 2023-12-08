from .forms import AccountCreationForm, LoginForm

def register_form(request):
    return {
        'register_form': AccountCreationForm
    }

def login_form(request):
    return {
        'login_form': LoginForm
    }