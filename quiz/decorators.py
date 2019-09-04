from django.contrib.auth.decorators import user_passes_test
from  users.models import Quizzers
from django.contrib.auth import REDIRECT_FIELD_NAME

def is_contributer(self):
    return self.is_contributer
def contributer_required(function=None,redirect_field_name=REDIRECT_FIELD_NAME,login_url='login'):
    actual_decorator=user_passes_test(lambda Quizzers:Quizzers.is_contributer and Quizzers.is_active,redirect_field_name=redirect_field_name,login_url=login_url)
    if function:
        return actual_decorator(function)
    return actual_decorator
def stud_required(function=None,redirect_field_name=REDIRECT_FIELD_NAME,login_url='login'):
    actual_decorator=user_passes_test(lambda Quizzers:Quizzers.is_stud and Quizzers.is_active,redirect_field_name=REDIRECT_FIELD_NAME,login_url='login')
    if function:
        return actual_decorator(function)
    return actual_decorator
