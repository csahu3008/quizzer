from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

from django.conf import settings
class Category(models.Model):
      title=models.CharField(_('Title'),max_length=40)
      def __str__(self):
          return self.title
class Quiz(models.Model):
    quiztitle=models.CharField(_('Title'),max_length=30,default=None)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    users_submitted=models.ManyToManyField(settings.AUTH_USER_MODEL)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='owner')
    level=(('SI','simple'),('MED','medium'),('HA','hard'))
    level=models.CharField(choices=level,max_length=3)
    def __str__(self):
        return  "Quiz {} with {} is added difficulty level is {}".format(self.id,self.category,self.get_level_display())
class Question(models.Model):
    questiontitle=models.CharField(_('Title'),max_length=400)
    op1=models.CharField(_('Option 1'),max_length=400)
    op2=models.CharField(_('Option 2'),max_length=400)
    op3=models.CharField(_('Option 3'),max_length=400)
    op4=models.CharField(_('Option 4'),max_length=400)
    answer=models.CharField(_('Answer'),max_length=400)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "{} is registered with {}".format(self.questiontitle,self.answer) 
    
class Score(models.Model):
    score=models.IntegerField()
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    studs=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    total_questions=models.IntegerField()
    def __str__(self):
        return "{} has scored {} in {}".format(self.studs,self.score,self.quiz)
    