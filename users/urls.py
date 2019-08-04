from django.urls import path
from .views import Signup,Login
urlpatterns = [
    path('',Signup,name='signup'),
    path('login/',Login,name='login')
]
