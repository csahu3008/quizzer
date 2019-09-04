from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from .models import Quizzers
class MyBackend:
    def authenticate(self,email,password):
        try:
            if email and password is not None:
                user=Quizzers.objects.get(email=email)
                if user is Not None:
                    if user.check_password(password):
                        return user
                    else:
                        return None
                else:
                    return None
            else:
                return user
        except Quizzers.DoesNotExist:
            return None
    def get_user(self,user_id):
        try:
            user=Quizzers.objects.get(pk=user_id)
            return user
        except Quizzers.DoesNotExist:
            return None

