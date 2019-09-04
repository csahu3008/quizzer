from django.urls import path,re_path
from .views import CreateQuiz,TakeQuiz,StartingPage,NextPages,Submit,MainPage
urlpatterns = [
    path('create/',CreateQuiz,name='create'),
    # path('<int:id>/takequiz/',TakeQuiz.as_view(),name='take'),
     path('takequiz/<int:pk>/',StartingPage.as_view(),name='start'),
     path('takequiz/main/<int:pk>/',NextPages.as_view(),name='next'),
     path('submit/',Submit,name='submit'),
     path('',MainPage.as_view(),name='main'),
     re_path(r'^(?P<id>[a-z-]*)/$',TakeQuiz.as_view(),name='take')
 
 ]
