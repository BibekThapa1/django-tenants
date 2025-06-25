from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Organization

# Register your models here.
@admin.register(Organization,admin.ModelAdmin)
class OrganizationAdmin(TenantAdminMixin):
    list_display = ("org_name",)