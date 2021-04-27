from django.db import models
from django.db import models
from django.db.models import Sum

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    house_no = models.CharField(max_length=200,null=True)
    room_rent = models.FloatField()
    electricity = models.FloatField()
    wifi = models.FloatField()     
    def __str__(self):
        return self.name

class Landlord(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    house_no = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Rent(models.Model):
    tenant=models.ForeignKey(Tenant, null=True, on_delete=models.SET_NULL)
    landlord=models.ForeignKey(Landlord, null=True, on_delete=models.SET_NULL)
    date_created= models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.tenant.name or ''
        

    



 

# Create your models here.
