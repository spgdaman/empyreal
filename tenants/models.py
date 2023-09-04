from django.db import models
# from django_multitenant.fields import *
# from django_multitenant.models import *
from django_tenants.models import TenantMixin, DomainMixin
# Create your models here.

class Tenant(TenantMixin):
    name = models.CharField(max_length=50)
    admin_first_name = models.CharField(max_length=50)
    admin_last_name = models.CharField(max_length=50)
    admin_email = models.CharField(max_length=50)
    admin_phone_number = models.IntegerField(null=False, blank=False)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Domain(DomainMixin):
    pass