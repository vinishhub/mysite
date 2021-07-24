from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    address=models.CharField(blank=False,null=True,max_length=255)
    birth_date=models.DateTimeField(blank=True)
    changed_on=models.DateTimeField(blank=False,auto_now=True)
    created_om=models.DateTimeField(blank=False,auto_now_add=True)

    def __str__(self):
        return self.address


