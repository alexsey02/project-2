from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user
        
    def create_superuser(self,email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email,password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'

class Tag(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name