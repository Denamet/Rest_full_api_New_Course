from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin , BaseUserManager


class UserProfileManager(BaseUserManager):

    
    
    def create_user(self , email , name , password=None):
        if not email :
            raise ValueError ("User must have an email address ! ")
        

        email = self.normalize_email(email)
        user = self.model(email=email , name =name)
        user.set_password(password)
        user.save(using = self._db)
        
        
        return user
    
 
    def create_superuser(self , email , name , password):
        user = self.create_user(email , name , password)
        user.is_superuser = True 
        user.is_staff = True 
        user.save(using=self._db)
        return user 


class User_profiels(AbstractBaseUser , PermissionsMixin) :
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=100 )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects1 = UserProfileManager()

    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        return self.email 

    def get_smal_name(self):
        return self.name 


    def __str__(self) :
        return self.email


