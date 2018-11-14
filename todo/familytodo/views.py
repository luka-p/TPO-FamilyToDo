from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q


from .forms import (FamilyRegistrationForm,
                    FamilyLoginForm,
                    ChildLoginForm,
                    ChildAddForm,
                    TaskAddForm)

from .models import (Family,
                     Parent,
                     Child,
                     Task)

def index(request):
    return render(request, 'index.html')

@require_http_methods(["GET", "POST"])
def register_family(request):
    if request.method == 'POST':
        form = FamilyRegistrationForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            family = Family(family_name=f['family_name'],
                            password=f['family_password'],
                            easy_password=f['family_easy_password'])
            if family is not None:
                family.save()
            father = Parent(parent_name=f['father_name'],
                   parent_family=family)
            if father is not None:
                father.save()
            mother = Parent(parent_name=f['mother_name'],
                   parent_family=family)
            if father is not None:
                father.save()
            if mother is not None:
                mother.save()
            return HttpResponseRedirect('')
    else:
        form = FamilyRegistrationForm()
        return render(request, 'family_register.html', {'form': form})

    return render(request, 'error.html')

@require_http_methods(["GET", "POST"])
def login_parent(request):
    if request.method == 'POST':
        form = FamilyLoginForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            try:
                family = Family.objects.get(family_name=f['family_name'])
                family_parents = [p.parent_name for p in Parent.objects.filter(parent_family=family)]
                if family.password == f['family_password'] and f['family_parent'] in family_parents:
                    family_name = f['family_name'] 
                    parent_name = f['family_parent']
                    request.session['family_name'] = family_name
                    request.session['parent_name'] = parent_name
                    return redirect('task-add')
            except:
                raise
            return HttpResponseRedirect('')
    else:
        form = FamilyLoginForm()
        return render(request, 'parent_login.html', {'form': form})

    return render(request, 'error.html')

@require_http_methods(["GET", "POST"])
def login_child(request):
    if request.method == 'POST':
        form = ChildLoginForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            try:
                family = Family.objects.get(family_name=f['family_name'])
                if family.easy_password == f['family_easy_password']:
                    family_name = f['family_name'] 
                    request.session['family_name'] = family_name
                    return redirect('task-display')
            except:
                raise
            return HttpResponseRedirect('')
    else:
        form = ChildLoginForm()
        return render(request, 'child_login.html', {'form': form})

    return render(request, 'error.html')

@require_http_methods(["GET"])
def display_task(request):
    family_name = request.session.get('family_name')
    qf = Q(family_name__in=[family_name])
    family = Family.objects.get(qf)
    existing_tasks = [t for t in Task.objects.filter(task_family=family)]
    return render(request, 'task_display.html', {'family': family_name, 'tasks': existing_tasks})

@require_http_methods(["GET", "POST"])
def add_task(request):
    if request.method == 'POST':
        taskform = TaskAddForm(request.POST)
        childform = ChildAddForm(request.POST)
        family_name = request.session.get('family_name')
        if taskform.is_valid():
            f = taskform.cleaned_data
            qf = Q(family_name__in=[family_name])
            qk = Q(child_name__in=[f['task_child']])
            family = Family.objects.get(qf)
            child = Child.objects.get(qf and qk)
            task = Task(task_name=f['task_name'], task_family=family, task_importance=f['task_importance'],
                        task_reward=f['task_reward'], task_due=f['task_due'], task_child=child,
                        task_complete=False)
            if task is not None:
                task.save()
        if childform.is_valid():
            f = childform.cleaned_data
            qf = Q(family_name__in=[family_name])
            family = Family.objects.get(qf)
            child = Child(child_name=f['child_name'], child_family=family)
            if child is not None:
                child.save()
        request.session['family_name'] = family_name
        return redirect('task-add') 
    else:
        family_name = request.session.get('family_name')
        parent_name = request.session.get('parent_name')
        family = Family.objects.get(family_name=family_name)
        family_kids = [(c.child_name, c.child_name) for c in Child.objects.filter(child_family=family)] 
        existing_tasks = [t for t in Task.objects.filter(task_family=family)]
        child_form = ChildAddForm()
        task_form = TaskAddForm()
        if len(family_kids) != 0:
            task_form.fields['task_child'].choices = family_kids
            task_form.fields['task_child'].initial = family_kids[0] 
        else:
            task_form.fields['task_child'].choices = [('-------','-------')]
            task_form.fields['task_child'].initial =  ('-------','-------')
        return render(request, 'task_add.html',
                {'task_form': task_form, 'child_form': child_form, 
                 'family': family_name, 'parent': parent_name,
                 'tasks': existing_tasks})

    return render(request, 'error.html')
