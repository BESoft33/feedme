from django.contrib.auth.models import BaseUserManager
from applications.user_handler import models

class UserManager(BaseUserManager):
    def create_superuser(self, email=None, password=None, **extra_fields):
        
        if email is None:
            raise ValueError("Email is a required field.")
        if not password:
            raise ValueError("Can't create User without a password!")
        
        
        user = self.model(
            email=self.normalize_email(email),
        )                
        
        user.is_staff       = True
        user.is_superuser   = True 
        
        user.set_password(password)
        
        user.save(using=self._db)
        
        return user 
    
    def create_staffuser(self, email = None, phone = None, password=None, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        
        if email is None:
            raise ValueError("Email is a required field.")
        if not password:
            raise ValueError("Can't create User without a password!")
        
        
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )
        user.is_staff = True
        
        user.set_password(password)
        
        user.save(using=self._db)
        
        return user 
    
    def create_user(self, email=None, phone = None, password=None, **extra_fields):
        
        if password is None:
            raise ValueError("Can't create User without a password!")
        
        if email is None and phone is None:
            raise ValueError("At least Email or Phone is required.")

        
        elif phone is None:
            #only email is provided
            user = self.model(
                email   =self.normalize_email(email),
            )
        elif email is None:
            #only phone is provided
            user = self.model(
                phone = phone,
            )
        else:
            user = self.model(
                email = self.normalize_email(email),
                phone = phone
                )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomerManager(UserManager):
    def create_user(self, email=None, phone = None, password=None, **extra_fields):
        return super().create_user(email=email, phone=phone,password=password, **extra_fields)

    def get_queryset(self):
        return super().get_queryset().filter(role=models.User.CUSTOMER)

class RestaurantAdminManager(UserManager):
    def create_user(self, email=None, phone = None, password=None, **extra_fields):
        return super().create_staffuser(email=email,phone=phone,password=password, **extra_fields)
        

    def get_queryset(self):
        return super().get_queryset().filter(role=models.User.RESTAURANT_ADMIN)

class AdminManager(UserManager):
    def create_user(self, email=None, phone = None, password=None, **extra_fields):
        return super().create_superuser(email=email,phone=phone,password=password, **extra_fields)
        

    def get_queryset(self):
        return super().get_queryset().filter(role=models.User.PROJECT_ADMIN)