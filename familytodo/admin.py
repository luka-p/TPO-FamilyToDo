from django.contrib import admin
from .models import Family, Parent, Child, Task

''' Admin model register '''
@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    ''' columns to display on admin page '''
    list_display=['family_name', 'ac_type', 'family_username', 'password', 'easy_password']

''' Parent model register '''
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    ''' columns to display on admin page '''
    list_display=['parent_name', 'parent_family']

''' Child model register '''
@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    ''' columns to display on admin page '''
    list_display=['child_name', 'child_family']

''' Task model register '''
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ''' columns to display on admin page '''
    list_display=['task_name', 'task_complete', 'task_importance', 'task_reward', 'task_due', 'task_family', 'task_child'] 

