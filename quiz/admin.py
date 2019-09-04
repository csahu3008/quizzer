from django.contrib import admin
from django.contrib.admin import StackedInline
from .models import Category,Question,Quiz,Score

class QuestionStackedInline(admin.StackedInline):
    model=Question
class QuizAdmin(admin.ModelAdmin):
    list_display=['category','level']
    inlines=[QuestionStackedInline, ]
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Category)
admin.site.register(Score)