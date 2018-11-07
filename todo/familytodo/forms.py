from django import forms

''' Family registration form '''
class FamilyRegistrationForm(forms.Form):
    ''' Family name and passwords '''
    family_name = forms.CharField(label="Family name", max_length=30, strip=True)
    family_password = forms.CharField(label="Full password", max_length=30, widget=forms.PasswordInput)
    family_easy_password = forms.IntegerField(label="Easy password", min_value=0000, max_value=9999, widget=forms.PasswordInput)
    
    ''' Family parents '''
    father_name = forms.CharField(label="Father name", max_length=30, strip=True)
    mother_name = forms.CharField(label="Mother name", max_length=30, strip=True)

''' Family login form '''
class FamilyLoginForm(forms.Form):
    family_name = forms.CharField(label="Family name", max_length=30, strip=True)
    family_parent = forms.CharField(label="Parent name", max_length=30m strip=True)
    family_password = forms.CharField(label="Family password", max_length=30, widget=forms.PasswordInput)

''' Child login form '''
class ChildLoginForm(forms.Form):
    family_name = forms.CharField(label="Family name", max_length=30, strip=True)
    family_easy_password = forms.IntegerField(label="Family password", min_value=0000, max_value=9999, widget=forms.PasswordInput)
