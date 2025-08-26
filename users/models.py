# users/models.py
from django.contrib.auth.models import AbstractBaseUser  , PermissionsMixin ,BaseUserManager
from django.db import models
from django.core.exceptions import ValidationError


class CostumUserManager(BaseUserManager):
    # create a method for creating user
    def create_user(self,username,email,password=None):
        
        #  lets check email and username in first
        if not email :
           raise ValueError("Email is required")
       
        if not username:
            raise ValueError("Username is required")
        
        email = self.normalize_email(email)
    
        # lets create a user model 
        user = self.model(email=email,username=username)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, username, password):
     user = self.create_user(email, username, password)
     user.is_staff = True
     user.is_superuser = True
     user.save(using=self._db)
     return user

  
# -----------------------
# Custom User Model
# -----------------------

class CostumUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(unique=True,max_length=125,)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    # link this costom user with its manager to mange him in term of database 
    # becouse django cant manage a custome user created by a programmer so i created a manger to mange it
    objects = CostumUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email





class Customerprofile(models.Model):
    user = models.OneToOneField(CostumUser,on_delete=models.CASCADE,related_name="customer_profile")
    date_of_birth = models.DateField()
    
    def __str__(self):
        return f"{self.user.username} (Customer)"
    
    

class CompanyProfile(models.Model):
    # shoud respect the subject  fiels of work
    FIELD_OF_WORK_CHOICES = [
        ('Air Conditioner', 'Air Conditioner'),
        ('All in One', 'All in One'),
        ('Carpentry', 'Carpentry'),
        ('Electricity', 'Electricity'),
        ('Gardening', 'Gardening'),
        ('Home Machines', 'Home Machines'),
        ('Housekeeping', 'Housekeeping'),
        ('Interior Design', 'Interior Design'),
        ('Locks', 'Locks'),
        ('Painting', 'Painting'),
        ('Plumbing', 'Plumbing'),
        ('Water Heaters', 'Water Heaters'),
    ]
    

    user = models.OneToOneField(CostumUser, on_delete=models.CASCADE, related_name="company_profile")
    field_of_work = models.CharField(max_length=255, choices=FIELD_OF_WORK_CHOICES)
    def clean(self):
        # Ensure the field_of_work is one of the valid choices
        if self.field_of_work not in dict(self.FIELD_OF_WORK_CHOICES):
            raise ValidationError({'field_of_work': 'Invalid field of work selection'})


    def __str__(self):
        return f"{self.user.username} (Company)"
