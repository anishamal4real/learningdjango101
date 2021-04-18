from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Tenant)
admin.site.register(Landlord)
admin.site.register(Rent)