from django.contrib import admin
from .models import Quizzers
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.contrib.auth.admin import UserAdmin
from .forms import CreateForm,ChangeForm
class Quizzer(UserAdmin):
    add_form=CreateForm
    form=ChangeForm
    ordering=('email','mobile')
    list_display=['email','name']
    filter=('is_active','is_cotributer','is_stud')
    add_fieldsets=(
        (None,{'classes':('wide',),'fields':('email','mobile','name','password1','password2')}),
    )
    fieldsets=(
        (None,{'fields':('name','email','password','mobile')}),('Designation',{'fields':('is_superuser','user_permissions','is_active','is_stud','is_contributer')})
    )
admin.site.register(Quizzers,Quizzer)
