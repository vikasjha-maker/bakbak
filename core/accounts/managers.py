from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _



class CustomUserManager(BaseUserManager):


    def create_user(self, email, password,**extra_fields):
        """
        Creates and saves a staff user with the given emoail and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password,**extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError()(_("Super must have is_staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError()(_("Super must have is_super=True."))
        
        return  self.create_user(email,password,**extra_fields)
