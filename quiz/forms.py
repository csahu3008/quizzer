from django import forms
from .models import Category,Question,Quiz
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=('questiontitle','op1','op2','op3','op4','answer')
    # widget=forms.TextInput(attrs={'required':False})
class QuizForm(forms.ModelForm):
    class Meta:
        model=Quiz
        fields=('quiztitle','category','level')