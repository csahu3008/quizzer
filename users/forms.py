from django import forms
from django.utils.translation import ugettext as _
from users.models import Quizzers
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
class CreateForm(forms.ModelForm):
    class Meta:
        model=Quizzers
        fields=('name','email','mobile','password1')
    name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id':'name'}))
    email=forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'id':'email'}))
    password1=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'id':'password'}))
    password2=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'id':'password2'}))
    mobile=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'id':'mobile'}))
    def clean_password2(self):
        p1=self.cleaned_data['password1']
        p2=self.cleaned_data['password2']
        if p1 != p2:
            raise forms.ValidationError(_("Sorry Passwords don not match"))
    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))       
        if commit:
            print('hello')
            user.save()
        return user
class ChangeForm(forms.ModelForm):
    class Meta:
        model=Quizzers
        fields='__all__'
    password1=ReadOnlyPasswordHashField()
    def clean_password(self):
        return self.initial['password']

class LoginForm(forms.Form):
    email=forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'id':'email'}))
    password=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'id':'password'}))