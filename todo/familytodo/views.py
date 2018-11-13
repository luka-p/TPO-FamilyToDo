from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import render


from .forms import (FamilyRegistrationForm,
                    FamilyLoginForm,
                    ChildLoginForm,
                    TaskAddForm)

from .models import (Family,
                     Parent,
                     Child,
                     Task)

def index(request):
    return None

@require_http_methods(["GET", "POST"])
def register_family(request):
    if request.method == 'POST':
        form = FamilyRegistrationForm(request.POST)
        if form.is_valid():
            form_data=form.cleaned_data
            family = Family(family_name=form_data['family_name'],
                            password=form_data['family_password'],
                            easy_password=form_data['family_easy_password'])
            if family is not None:
                family.save()
            father = Parent(parent_name=form_data['father_name'],
                   parent_family=family)
            if father is not None:
                father.save()
            mother = Parent(parent_name=form_data['mother_name'],
                   parent_family=family)
            if father is not None:
                father.save()
            if mother is not None:
                mother.save()
            return HttpResponseRedirect('')
    else:
        form = FamilyRegistrationForm()

    return render(request, 'family_register.html', {'form': form})

@require_http_methods(["GET", "POST"])
def login_parent(request):
    if request.method == 'POST':
        form = FamilyLoginForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('')
    else:
        form = FamilyLoginForm()

    return render(request, 'parent_login.html', {'form': form})

@require_http_methods(["GET", "POST"])
def login_child(request):
    if request.method == 'POST':
        form = ChildLoginForm(request.POST)
        if form.is_valid():
            
            return HttpResponseRedirect('')
    else:
        form = ChildLoginForm()

    return render(request, 'child_login.html', {'form': form})

@require_http_methods(["GET", "POST"])
def add_task(request):
    if request.method == 'POST':
        form = TaskAddForm(request.POST)
        if form.is_valid():
            
            return HttpResponseRedirect('')
    else:
        form = TaskAddForm()

    return render(request, 'task-add.html', {'form': form})
