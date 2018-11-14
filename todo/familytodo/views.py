from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


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
            form_data = form.cleaned_data
            try:
                family = Family.objects.get(family_name=form_data['family_name'])
                family_parents = [p.parent_name for p in Parent.objects.filter(parent_family=family)]
                if family.password == form_data['family_password'] and form_data['family_parent'] in family_parents:
                    family_name = form_data['family_name'] 
                    parent_name = form_data['family_parent']
                    request.session['family_name'] = family_name
                    request.session['parent_name'] = parent_name
                    return redirect('task-add')
            except:
                raise
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
            f = form.cleaned_data
            print(f)
            family = Family.objects.get(family_name=f['task_family'])
            task = Task(task_name=f['task_name'], task_family=family, task_importance=f['task_importance'], task_reward=f['task_reward'], task_due=f['task_due'], task_child=f['task_child'], task_complete=False)
            if task is not None:
                task.save()
            return HttpResponseRedirect('')
    else:
        family_name = request.session.get('family_name')
        parent_name = request.session.get('parent_name')
        family = Family.objects.get(family_name=family_name)
        family_kids = [(c.child_name, c.child_name) for c in Child.objects.filter(child_family=family)] 
        existing_tasks = [t for t in Task.objects.filter(task_family=family)]
        child_form = ChildAddForm()
        task_form = TaskAddForm()
        task_form.fields['task_child'].choices = family_kids
        task_form.fields['task_child'].initial = family_kids[0] 
        task_form.fields['task_family'].initial = family_name 
        return render(request, 'control-panel.html',
                {'task_form': task_form, 'child_form': child_form, 
                 'family': family_name, 'parent': parent_name,
                 'tasks': existing_tasks})

    return render(request, 'error.html')
