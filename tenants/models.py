from django.db import models
from django_multitenant.fields import *
from django_multitenant.models import *
# Create your models here.

class Tenant(TenantModel):
    name = models.CharField(max_length=50)
    admin_first_name = models.CharField(max_length=50)
    admin_last_name = models.CharField(max_length=50)
    admin_email = models.CharField(max_length=50)
    admin_phone_number = models.IntegerField(null=False, blank=False)
    class TenantMeta:
        tenant_field_name = "id"