from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager (BaseUserManager):
    def create_user(self,email, password=None, name=None, lastname=None, is_active = True, is_staff = False, is_admin = False):
        if not email:
            errormsg=gettext("Users must have an email address")
            raise ValueError (errormsg)
        if not password:
            errormsg=gettext("Users must have a password")
            raise ValueError (errormsg)
        
        user = self.model (
            email=self.normalize_email(email))    
        user.set_password(password) # <-- this is how to assign and change the password

        name=name
        lastname=lastname 
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self,email, name=None, lastname=None,password=None):
        # user=self.create_user(email,name=None, lastname=None, password=password, is_staff = True)
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,email, name=None, lastname=None, password=None):
        #user=self.create_user(email, name=None, lastname=None, password=password, is_staff = True, is_admin = True)
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    name        = models.CharField(max_length=255, blank=True, null=True)
    lastname    = models.CharField(max_length=255, blank=True, null=True)
    active      = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)  #none Superuser
    admin       = models.BooleanField(default=False)  # Superuser
    timestamp   = models.DateTimeField(auto_now_add=True)
    #confirm    = models.BooleanField(default=False)
    #confirm_date = models.DateTimeField(auto_now=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # by default USERNAME_FIELD & password are required.. BTW password is default on AbstractBaseUser
    # Inlcude REQUIRE FIELD for other required fields.... this is only for User model customized
    REQUIRED_FIELDS = []  

    def __str__(self):
        return  self.email

    def get_full_name(self):
        return self.name+ " "+self.lastname
        
    def get_short_name(self):
        return self.name
            
    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff
    @property
    def is_active(self):
        return self.active
    @property
    def is_admin(self):
        return self.admin
    

# class profile(models.Model):
#     User        = models.OneToOneField(User, on_delete=models.CASCADE)
#     # extradata


class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

