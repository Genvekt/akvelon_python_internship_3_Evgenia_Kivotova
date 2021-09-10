from django.db import models
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save ordnary User with the given email and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_staffuser(self, email, password, **extra_fields):
        """
        Create and save a new admin User with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Staffuser must have is_staff=True'))

        return self.create_user(
            email,
            password=password,
            **extra_fields
        )

    def create_superuser(self, email, password,  **extra_fields):
        """
        Create and save a new superuser User with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        return self.create_user(
            email,
            password=password,
            **extra_fields
        )


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    
class Transaction(models.Model):

    # We will not create id, because Django creates this attribute by default
    # id = models.IntegerField(primary_key=True)

    # User ID - foreign key, that mask be linked to the User object. Therefore,
    #    by deleting User object service must delete all their transaction
    #    records as well.  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # Amount - simple float field, amount is not required to be integer
    amount = models.FloatField()

    # Date - Datetime field which will by default will have value 
    #   datetime.now(). `auto_now_add` parameter enables default feature
    #   only at the moment of record addition.
    date = models.DateField()

