from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class UserModel(AbstractUser):

    is_agent = models.BooleanField(default=False)
    referrer_id = models.CharField(max_length=30, null=True, blank=True)
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    profile_img = models.ImageField(default='default.png', upload_to='profile_images/')
    commission_earned = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    
    def generate_referer_id(self):
        if not self.referrer_id:
            self.referrer_id = str(uuid.uuid4())[:10]

    def calculate_commission(self):
        return self.get_total_number_of_referals() * 100 
    
    def get_total_number_of_referals(self):
        return self.referrals.all().count()
    
    def get_refferals(self):

        return self.referrals.all()
    
    def save(self, *args, **kwargs):
        if not self.is_superuser:
            self.generate_referer_id()

            # 
        return super().save(*args, **kwargs)
    


class Referral(models.Model):
    STATUS = (
        ('PENDING', 'PENDING'),
        ('ACTIVE', 'ACTIVE'),
        ('DOWN', 'DOWN')
    )
    referring_user = models.ForeignKey(UserModel, related_name='referrals', on_delete=models.CASCADE)
    referred_user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_redeemed = models.BooleanField(default=False)
    clear = models.BooleanField(default=False)






    


