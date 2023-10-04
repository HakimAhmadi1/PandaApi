from django.db import models
from django.contrib.auth.models import User
from employer.models import Jobs
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, phone, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_user(self, email, password,first_name, last_name, phone,  **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password,first_name, last_name, phone, **extra_fields)
    
    def create_superuser(self, email, password,first_name=None, last_name=None, phone=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password,first_name, last_name, phone,  **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100, default=None, null=True) 
    phone = models.CharField(max_length=20, default=None, null=True)  
    first_name = models.CharField(max_length=100, default=None, null=True)
    last_name = models.CharField(max_length=100, default=None, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser  = models.BooleanField(default=False)

    is_seeker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class ContactUs(models.Model):

    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
