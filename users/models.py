from django.db import models
# from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import BaseUserManager,User,AbstractUser
# Create your models here.
class ManageQuizzers(BaseUserManager):
    def create_stud(self,email,mobile,name,password=None,**extra_fieids):
        if not email:
            raise ValueError ("Email can not be left empty")
        email=self.normalize_email(email)
        extra_fieids.setdefault('is_staff',True)
        if extra_fieids.get('is_staff') is not True:
            raise ValueError("User Must Be staff")
        extra_fieids.setdefault('is_stud',True)
        stud=self.model(email=email,mobile=mobile,name=name,**extra_fieids)
        stud.set_password(password)
        stud.save()
        return stud
    def create_contributer(self,email,mobile,name,password=None,**extra_fieids):
        if not email:
            raise ValueError ("Email can not be left empty")
        email=self.normalize_email(email)
        extra_fieids.setdefault('is_staff',True)
        if extra_fieids.get('is_staff') is not True:
            raise ValueError("User Must Be staff")
        extra_fieids.setdefault('is_contributer',True)
        if extra_fieids.get('is_contributer') is not True:
            raise ValueError("User Must Be Contributer")
        extra_fieids.setdefault('is_stud',True)
        contributer=self.model(email=email,mobile=mobile,name=name,**extra_fieids)
        contributer.set_password(password)
        contributer.save()
        return contributer
    def create_superuser(self,email,mobile,name,password,**extra_fieids):
        extra_fieids.setdefault('is_contributer',True)
        extra_fieids.setdefault('is_superuser',True)
        extra_fieids.setdefault('is_active',True)
        if extra_fieids.get('is_superuser') is not True:
            raise ValueError("User Must Be superuser")
        if extra_fieids.get('is_active') is not True:
            raise ValueError("User Must Be active")
        if extra_fieids.get('is_contributer') is not True:
            raise ValueError("User Must Be A contributer")
        self.create_stud(email,mobile,name,password,**extra_fieids)

class Quizzers(AbstractUser):
    name=models.CharField(_('Name'),max_length=50)
    email=models.EmailField(_('Email'),unique=True,max_length=100)
    password1=models.CharField(_('Password'),max_length=40)
    mobile=models.CharField(_('Mobile Number'),max_length=10)
    is_active=models.BooleanField(_('Active User'),default=True)
    is_contributer=models.BooleanField(_('Contributer'),default=False)
    is_stud=models.BooleanField(_('Stud'),default=False)
    USERNAME_FIELD='email'
    username=None
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=['name','mobile']
    objects=ManageQuizzers()
    class Meta:
        verbose_name_plural='Quizzers'
    def __str__(self):
        return self.name
    @property
    def Contributer(self):
        return self.is_contributer
    @property
    def Stud(self):
        return self.is_stud
