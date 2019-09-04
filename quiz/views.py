from django.shortcuts import render,HttpResponse,redirect,get_list_or_404,get_object_or_404
from django.http import JsonResponse
from .forms import QuizForm,QuestionForm
from django.db.models import Q
from django.views.generic.edit import SingleObjectMixin
from django.contrib.messages import success
from django.forms import formset_factory
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView,ListView,DetailView,View,CreateView,FormView
from .models import Category,Question,Quiz,Score
from quiz.decorators import contributer_required,stud_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
score=0
@login_required
@contributer_required
def CreateQuiz(request,new_context={}):
    QusetionFormsSet=formset_factory(QuestionForm)
    if request.method=='POST':
        formset=QusetionFormsSet(request.POST,prefix='form')
        quiz=QuizForm(request.POST)
        if quiz.is_valid() and formset.is_valid():
            sample=quiz.save(commit=False)
            sample.created_by=request.user
            sample.save()
            data=[ d for d in formset.cleaned_data]
            for form in formset:
                k=form.save(commit=False)
                k.quiz=sample
                k.save()
            return redirect('/')
        
    else:
        data={
            'form-TOTAL_FORMS':'1',
            'form-INITIAL_FORMS':'0',
            'form-MAX_NUM_FORMS':'',
            'form-MIN_NUM_FORMS':'',
        }
        formset=QusetionFormsSet(data,prefix='form')
        context={'form1':QuizForm,'formset':formset}
        new_context.update(context)
    return render(request,'create_quiz.html',new_context)

def Submit(request):
    global score
    if(request.method=='POST'):
        if(request.session['track']):
            useranswer=request.POST['option-selected']
            question=Quiz.objects.get(quiztitle=request.session['track']).question_set.get(id=request.POST['qno'])
            if(question.answer==useranswer):
                score+=1
            else:
                pass
            return JsonResponse({'success':"processes successful"})
        else:
            return JsonResponse({'failed':'failed request'})
@method_decorator(login_required,name='dispatch')
@method_decorator(stud_required,name='dispatch')
class TakeQuiz(ListView):
    template_name='quiz_list.html'
    model=Quiz
    def get_queryset(self,**kwargs):
        query=super().get_queryset()
        return query.filter(category__title__iexact=self.kwargs['id'].replace('-',' '))
    def dispatch(self,request,**kwargs):
        global score
        if 'track' in request.session:
            success(self.request,"Your Score is {}".format(score))
            success(self.request,"Your response has been Successfully updated")
            quiz=Quiz.objects.get(quiztitle=request.session['track'])
            Score.objects.create(score=score,quiz=quiz,studs=request.user,total_questions=quiz.question_set.all().count())
            score=0
            del request.session['track']     
        return super().dispatch(request,**kwargs)
class StartingPage(DetailView):
    template_name='detail_quiz.html'    
    model=Quiz
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['first']=self.get_object().question_set.first()
        context['last']=self.get_object().question_set.last().id
        return context
    def dispatch(self,request,**kwargs):
        global score
        request.session['track']=self.get_object().quiztitle
        return super().dispatch(request,**kwargs)


class NextPages(DetailView):
    template_name='detail_quiz2.html'
    model=Question
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['last_question']=self.get_object().quiz.question_set.last().id
        return context
    def dispatch(self,request,**kwargs):
        if(request.session['track']):
            if(request.session['track']==self.get_object().quiz.quiztitle):
                pass
            else:
                raise PermissionDenied
        else:
            raise PermissionDenied
        return super().dispatch(request,**kwargs)

class MainPage(ListView):
    template_name='main.html'
    model=Category