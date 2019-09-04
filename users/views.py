from django.shortcuts import render,HttpResponse,redirect,reverse,resolve_url
from django.http import JsonResponse
from .models import Quizzers
from django.db.models import Q
from django.contrib.contenttypes.models import  ContentType
from django.contrib.auth.models import Permission
from django.contrib import messages
from quiz.models import Category,Question,Quiz
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
            print(contributer)
            if status:
                contributer.is_contributer=p
                contributer.is_stud=True
                contributer.is_staff=True 
                c1=ContentType.objects.get_for_model(Quiz)
                c2=ContentType.objects.get_for_model(Question)
                permissions=Permission.objects.filter(Q(content_type=c1)|Q(content_type=c2))
                contributer.user_permissions.set(permissions)
            else:
                contributer.is_stud=p
                contributer.is_staff=True
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
    if request.session.get('email'):
        return redirect('/') 
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
                    return redirect('/')
                else:
                    if user.is_stud:
                        request.session['email']=email
                        login(request,user)
                        return redirect('/')
            else:
                return HttpResponse('Invalid credential details were entered ,Try again')
        else:
            return HttpResponse("You have attempted an incorrect details")
    else:
        form=LoginForm()
        return render(request,'registration/login.html',{'form':form})



