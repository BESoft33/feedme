from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# from .managers import CustomerManager, RestaurantAdminManager, AdminManager
from . import managers

class User(AbstractBaseUser, PermissionsMixin):
    
    RESTAURANT_ADMIN    = 1 
    CUSTOMER            = 2
    PROJECT_ADMIN       = 3

    ROLE_CHOICES = (
        (RESTAURANT_ADMIN,'Restaurant Manager'),
        (CUSTOMER, 'Customer'),
        (PROJECT_ADMIN,'Project Admin')
    )

    email           = models.EmailField(max_length=255, unique=True)
    phone           = models.CharField(max_length=14, unique=True, null=True, blank=True)
    role            = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, default=CUSTOMER)
    date_joined     = models.DateTimeField(auto_now_add=True)
    is_staff        = models.BooleanField(default=False) 
    is_superuser    = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    
    admins = managers.AdminManager()
    managers = managers.RestaurantAdminManager()
    customers = managers.CustomerManager()
    users = managers.UserManager()
    
    USERNAME_FIELD: str     ='email'
    REQUIRED_FIELDS: list   =['password']
