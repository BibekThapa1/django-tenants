from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
from public.models import Client

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("The email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("user_type",CustomUser.UserType.SUPER_ADMIN)
        return self.create_user(email,password,**extra_fields)
        

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    class UserType(models.TextChoices):
        SUPER_ADMIN="super_admin","Super Admin"
        CONSULTANCY =  "consultancy","Consultancy"
        STUDENT = "student","Student"
        
    user_type = models.CharField(max_length=30,choices=UserType.choices,default=UserType.STUDENT)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name="client_users",null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
