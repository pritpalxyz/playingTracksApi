from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email 					= models.EmailField(
					        verbose_name='email address',
					        max_length	=255,
					        unique		=True,
    )
    
    first_name              = models.CharField(max_length=100)
    last_name               = models.CharField(max_length=100)
    is_active 				= models.BooleanField(default=True)
    is_admin 				= models.BooleanField(default=False)

    objects 				= MyUserManager()

    USERNAME_FIELD 			= 'email'
    REQUIRED_FIELDS 		= []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):              
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin