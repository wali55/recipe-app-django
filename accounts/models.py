from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, phone, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
            phone = phone,
        )

        user.set_password(password)
        user.save(self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, phone, password=None):
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            password = password,
        )

        user.is_admin = True
        user.save(self._db)
        return user
    

class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

