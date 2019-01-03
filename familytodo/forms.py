from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div, FieldWithButtons

from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

''' import child from models because this is dynamic
so it changes or can be changed every time that TaskAddForm is called
and because of that we need to refresh choices every time we call this form '''
from .models import Child
from .models import (IMPORTANCE,
                     ACTYPE)

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
    family_name = forms.CharField(label="Family name/surename", max_length=30, strip=True)
    family_username = forms.CharField(label="Family username", max_length=30, strip=True)
    family_password = forms.CharField(label="Full password", max_length=30, widget=forms.PasswordInput)
    family_easy_password = forms.IntegerField(label="Easy password", min_value=0000, max_value=9999, widget=forms.PasswordInput, error_messages=err_msg)
    account_type = forms.ChoiceField(label="Account type", choices=ACTYPE, widget=forms.RadioSelect)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('register', 'Register', css_class='btn-primary'))

class FreeParentForm(forms.Form):
    ''' Free users can add only one parent '''
    parent_name = forms.CharField(label="Parent name", max_length=30, strip=True)

class PaidParentForm(forms.Form):
    ''' Paid users can add two parents '''
    father_name = forms.CharField(label="Father name", max_length=30, strip=True)
    mother_name = forms.CharField(label="Mother name", max_length=30, strip=True)

''' Family login form '''
class FamilyLoginForm(forms.Form):
    family_username = forms.CharField(label="Family username", max_length=30, strip=True)
    family_parent = forms.CharField(label="Parent name", max_length=30, strip=True)
    family_password = forms.CharField(label="Family password", max_length=30, widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('login', 'Login', css_class='btn-primary'))

''' Child login form '''
class ChildLoginForm(forms.Form):
    family_username = forms.CharField(label="Family username", max_length=30, strip=True)
    family_easy_password = forms.IntegerField(label="Family password", min_value=0000, max_value=9999, widget=forms.PasswordInput, error_messages=err_msg)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('login', 'Login', css_class='btn-primary'))

''' Child add form '''
class ChildAddForm(forms.Form):
    child_name = forms.CharField(label="", max_length=30, strip=True,
    widget=forms.TextInput(attrs={'placeholder': 'Child name',
                                    'class': 'form-control-lg mr-2'}))
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        FieldWithButtons('child_name', StrictButton('+', type='submit', css_class=' btn btn-primary')),
    )
    #helper.add_input(Submit('submit', '+', css_class='btn-primary'))

''' Task adding form '''
class TaskAddForm(forms.Form):
    task_name = forms.CharField(label="Task name", max_length=30, strip=True)
    task_importance = forms.ChoiceField(label="Task importance", choices=IMPORTANCE, initial='MEDIUM')
    task_reward = forms.CharField(label="Task reward", max_length=30, strip=True, required=False)
    task_due = forms.IntegerField(label="Taks due days", min_value=0, error_messages=err_msg)
    task_child = forms.ChoiceField(label="Child", choices=[(c.child_name, c.child_name) for c in Child.objects.all()])

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Add/Save task', css_class='btn-primary'))
