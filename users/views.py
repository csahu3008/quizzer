from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Quizzers
from django.contrib import messages
from .forms import CreateForm,ChangeForm,LoginForm
from django.contrib.auth import login,authenticate
def Signup(request):
    if request.method=='POST':
        if 'is_contributer' in request.POST:
            p=request.POST['is_contributer']
            msg='Registed successfully as contributer'
            status=True
        else:
            p=request.POST['is_stud']
            status=False
            msg='Registed successfully as Stud'                
        form=CreateForm(request.POST)
        if form.is_valid():
            contributer=form.save()
            if status:
                contributer.is_contributer=p
            else:
                contributer.is_stud=p
            contributer.save()
            messages.success(request,msg)
            data={'status':status}
            return JsonResponse(data)
        else:
            errors= dict(form.errors.items())
            print(errors)
            data={'status':404,'errors':errors}
            return JsonResponse(data)
    else:
        form=CreateForm()
    return render(request,'registration/signup.html',context={'form':form})


def Login(request):
    # if request.session.get('email'):
    #     return HttpResponse("U Are already Logged in")
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,email=email,password=password)
            if user is not None:
                if user.is_contributer:
                    request.session['email']=email
                    login(request,user)
                    return HttpResponse('You are logged in successfully')
                else:
                    return HttpResponse('You are not recognize as Contributer')
            else:
                return HttpResponse('Invalid credential details were entered ,Try again')
        else:
            return HttpResponse("You have attempted an incorrect details")
    else:
        form=LoginForm()
        return render(request,'registration/login.html',{'form':form})



