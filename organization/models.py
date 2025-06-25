from django.db import models

# Create your models here.
class Organization(models.Model):
    org_name = models.CharField(max_length=100,null=True,blank=False)
    org_address = models.CharField(max_length=100,null=True,blank=False)
    org_phone = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.org_name