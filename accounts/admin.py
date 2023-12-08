from django.contrib import admin
from .models import UserModel,Referral

# Register your models here.
admin.site.register([UserModel, Referral])
