from django import forms

''' import child from models because this is dynamic
so it changes or can be changed every time that TaskAddForm is called
and because of that we need to refresh choices every time we call this form '''
from .models import Child
from .models import (IMPORTANCE,
                    CHILDREN,
                     ACTYPE,
                     DAYS)

''' error messages dict '''
err_msg = {
    'required': 'This field is required',
    'invalid': 'Enter valid input',
    'max_value': 'Please enter numeric password that is four digits long.',
    'min_value': 'Please enter numeric password that is four digits long.',
}

''' Family registration form '''
class FamilyRegistrationForm(forms.Form):
    ''' Family name, usename and passwords '''
    family_name = forms.CharField(label="Family name/surename", max_length=30, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Family name/surename'}))
    family_username = forms.CharField(label="Family username", max_length=30, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Family username'}))
    family_password = forms.CharField(label="Full password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Full password'}))
    family_easy_password = forms.IntegerField(label="Easy password", min_value=0000, max_value=9999, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Easy password'}), error_messages=err_msg)
    account_type = forms.ChoiceField(label="Account type", choices=ACTYPE, widget=forms.RadioSelect)


class FreeParentForm(forms.Form):
    ''' Free users can add only one parent '''
    parent_name = forms.CharField(label="Parent name", max_length=30, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Parent name'}))

class PaidParentForm(forms.Form):
    ''' Paid users can add two parents '''
    father_name = forms.CharField(label="Father name", max_length=30, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father name'}))
    mother_name = forms.CharField(label="Mother name", max_length=30, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother name'}))

''' Family login form '''
class FamilyLoginForm(forms.Form):
    family_username = forms.CharField(label="Family username", max_length=30, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Family username'}) )
    family_parent = forms.CharField(label="Parent name", max_length=30, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Parent name'}))
    family_password = forms.CharField(label="Family password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Family password'}))

''' Child login form '''
class ChildLoginForm(forms.Form):
    family_username = forms.CharField(label="Family username", max_length=30, strip=True)
    family_easy_password = forms.IntegerField(label="Family password", min_value=0000, max_value=9999, widget=forms.PasswordInput, error_messages=err_msg)

''' Child add form '''
class ChildAddForm(forms.Form):
    child_name = forms.CharField(label="Child name", max_length=30, strip=True)

''' Child select form '''
class ChildSelectForm(forms.Form):
    child_name = forms.ChoiceField(label="Child", choices=CHILDREN, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Child', 'onchange': 'this.form.submit()'}))

''' Task adding form '''
class TaskAddForm(forms.Form):
    task_name = forms.CharField(label="Task name", max_length=30, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task name'}))
    task_importance = forms.ChoiceField(label="Task importance", choices=IMPORTANCE, initial='MEDIUM', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Task importance'}))
    task_reward = forms.CharField(label="Task reward", max_length=30, strip=True, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task reward'}))
    task_due = forms.IntegerField(label="Taks due days", min_value=0, error_messages=err_msg, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Task due date'}))
    task_child = forms.ChoiceField(label="Child", choices=[], widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Child'}))

''' Schedule adding form '''
class ScheduleAddForm(forms.Form):
    sc_desc = forms.CharField(label="Schedule description", max_length=30, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Schedule description'}))
    sc_day = forms.ChoiceField(label="Day of the week", choices=DAYS, initial='MONDAY', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Day of the week'}))
    sc_time = forms.TimeField(label="Time", widget=forms.TimeInput(format='%H:%M', attrs={'class': 'form-control', 'placeholder': 'hh:mm'}))
    sc_child = forms.ChoiceField(label="Child", choices=[], widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Child'}))

