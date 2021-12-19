from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    """Manager for Custom User Model"""
    
    def create_user(self, email, username, password=None, **extra_kwargs):
        """Method to create client users"""
        
        if not email:
            raise ValueError(_('Email is required, please enter Email'))
        
        user = self.model(email=self.normalize_email(email), username=username, **extra_kwargs)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """Method to create admin users"""

        user = self.create_user(email=email, username=username, password=password)

        user.is_superuser = True

        user.save(using=self._db)

        return user
    


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model"""

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = UserManager()


    def __str__(self) -> str:
        return self.email
    
