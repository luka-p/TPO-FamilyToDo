from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import (FamilyRegistrationForm,
                    FamilyLoginForm,
                    ChildLoginForm,
                    TaskAddForm)

def index(request):
    return None

@require_http_methods(["GET", "POST"])
def register_family(request):
    if request.method == 'POST':
        form = FamilyRegistrationForm(request.POST)
        if form.is_valid():

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
