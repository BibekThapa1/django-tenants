from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.full_name