from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from django.db import IntegrityError

''' froms import from forms.py '''
from .forms import (FamilyRegistrationForm,
                    FamilyLoginForm,
                    ChildLoginForm,
                    ChildAddForm,
                    TaskAddForm)

''' models import from models.py '''
from .models import (Family,
                     Parent,
                     Child,
                     Task)

''' index view that just renders index.html nothing special '''
def index(request):
    return render(request, 'index.html')

''' register family view, display form and save inputed data into database '''
@require_http_methods(["GET", "POST"])
def register_family(request):
    ''' POST '''
    if request.method == 'POST':
        ''' fill the form with data and test if the form inputs are valid '''
        form = FamilyRegistrationForm(request.POST)
        if form.is_valid():
            ''' store data into a dict and create new family to save '''
            f = form.cleaned_data
            ''' try to create and save family '''
            try: 
                family = Family(family_name=f['family_name'],
                                family_username=f['family_username'],
                                password=f['family_password'],
                                easy_password=f['family_easy_password'])
                if family is not None:
                    family.save()
                ''' catch unique error '''
            except IntegrityError as ie:
                form = FamilyRegistrationForm()
                return render(request, 'family_register.html', {'form': form, 'error': 'Username already exists'})
            ''' construct and save father and mother '''
            father = Parent(parent_name=f['father_name'],
                   parent_family=family)
            if father is not None:
                father.save()
            mother = Parent(parent_name=f['mother_name'],
                   parent_family=family)
            if mother is not None:
                mother.save()
            ''' redirect back to the index page '''
            return redirect('index')
        ''' GET '''
    else:
        ''' create from and send it to the family_register family page '''
        form = FamilyRegistrationForm()

    ''' final return, renders html page with registration form '''
    return render(request, 'family_register.html', {'form': form})

''' parent login view for authentication of parent into control panel '''
@require_http_methods(["GET", "POST"])
def login_parent(request):
    ''' POST '''
    if request.method == 'POST':
        ''' fill the form and test if it is valid '''
        form = FamilyLoginForm(request.POST)
        if form.is_valid():
            ''' store data from form into dict '''
            f = form.cleaned_data
            try:
                ''' get family username and family parents '''
                family = Family.objects.get(family_username=f['family_username'])
                family_parents = [p.parent_name for p in Parent.objects.filter(parent_family=family)]
                ''' authentication by username and parent '''
                if family.password == f['family_password'] and f['family_parent'] in family_parents:
                    ''' extract important information from form '''
                    family_name = family.family_name 
                    family_username = f['family_username']
                    parent_name = f['family_parent']
                    ''' store authentication info into session data so we can pass values to another view '''
                    request.session['family_name'] = family_name
                    request.session['family_username'] = family_username
                    request.session['parent_name'] = parent_name
                    ''' redirect to control panel eg. task adding page '''
                    return redirect('task-add')
            except Exception as e:
                ''' handle exception with error msg '''
                form = FamilyLoginForm()
                return render(request, 'parent_login.html', {'form': form, 'error': 'Login error, check your credentials'})
        ''' GET '''
    else:
        ''' creation of an empty form '''
        form = FamilyLoginForm()

    ''' render form with parent login html '''
    return render(request, 'parent_login.html', {'form': form})

@require_http_methods(["GET", "POST"])
def add_task(request):
    ''' POST '''
    if request.method == 'POST':
        ''' fill data from html into forms '''
        taskform = TaskAddForm(request.POST)
        childform = ChildAddForm(request.POST)
        ''' from session data get user name and family name '''
        family_username = request.session.get('family_username')
        family_name = request.session.get('family_name')
        parent_name = request.session.get('parent_name')
        ''' construct empty forms '''
        child_form = ChildAddForm()
        task_form = TaskAddForm()
        ''' query that finds the specific family by its username '''
        qf = Q(family_username=family_username)
        ''' get family used in both forms, taks add and child add '''
        try:
            family = Family.objects.get(qf)
        except Exception as e:
            return render(request, 'task_add.html',
                    {'task_form': task_form, 'child_form': child_form, 
                     'family': family_name, 'parent': parent_name,
                     'tasks': existing_tasks, 'error': str(e)})
        ''' extract existing task for above family '''
        existing_tasks = [t for t in Task.objects.filter(task_family=family)]
        ''' first check if child can be added  to the family and then if we can add task '''
        ''' if children adding form is valid save that child into loged in family '''
        if childform.is_valid():
            f = childform.cleaned_data
            ''' if no children hasnt been added to the family display error '''
            if f['child_name'] == '-------': 
                return render(request, 'task_add.html',
                        {'task_form': task_form, 'child_form': child_form, 
                         'family': family_name, 'parent': parent_name,
                         'tasks': existing_tasks, 'error': 'Add atleast one child.'})
            child = Child(child_name=f['child_name'], child_family=family)
            if child is not None:
                child.save()
        ''' if form is valid then save task '''
        if taskform.is_valid():
            f = taskform.cleaned_data
            ''' try to get a child and add task to that child, except display error on the page '''
            try:
                child = Child.objects.get(child_family=family, child_name=f['task_child'])
                ''' construct task and save it if task can be saved '''
                task = Task(task_name=f['task_name'], task_family=family, task_importance=f['task_importance'],
                            task_reward=f['task_reward'], task_due=f['task_due'], task_child=child,
                            task_complete=False)
                if task is not None:
                    task.save()
            except Exception as e:
                ''' handle exception with error msg '''
                return render(request, 'task_add.html',
                        {'task_form': task_form, 'child_form': child_form, 
                         'family': family_name, 'parent': parent_name,
                         'tasks': existing_tasks, 'error': str(e)})
        ''' if all good then save username and family name/surname into sesstion data '''
        request.session['family_username'] = family_username
        request.session['family_name'] = family_name
        ''' in the end redirect back to itself with get method '''
        return redirect('task-add') 
        ''' GET '''
    else:
        ''' construct empty forms that will be render and modified '''
        child_form = ChildAddForm()
        task_form = TaskAddForm()
        ''' retrive family name, username and parent name from sesstion data '''
        family_name = request.session.get('family_name')
        family_username = request.session.get('family_username')
        parent_name = request.session.get('parent_name')
        ''' from db get family, kids from this family, existing tasks and construct child and taks form '''
        try:
            family = Family.objects.get(family_username=family_username)
        except Exception as e:
            ''' if getting the family from db by username failed display error on the page '''
            return render(request, 'task_add.html',
                    {'task_form': task_form, 'child_form': child_form, 
                     'family': family_name, 'parent': parent_name,
                     'tasks': existing_tasks, 'error': str(e)})
        family_kids = [(c.child_name, c.child_name) for c in Child.objects.filter(child_family=family)] 
        existing_tasks = [t for t in Task.objects.filter(task_family=family)]
        ''' if family has no children added yet display ------ else fill choices with family children '''
        if len(family_kids) != 0:
            task_form.fields['task_child'].choices = family_kids
            task_form.fields['task_child'].initial = family_kids[0] 
        else:
            task_form.fields['task_child'].choices = [('-------','-------')]
            task_form.fields['task_child'].initial =  ('-------','-------')
        ''' return and render html template with all data from above '''
        return render(request, 'task_add.html',
                {'task_form': task_form, 'child_form': child_form, 
                 'family': family_name, 'parent': parent_name,
                 'tasks': existing_tasks})

    ''' error page if view failed '''
    return render(request, 'error.html')

@require_http_methods(["GET", "POST"])
def login_child(request):
    if request.method == 'POST':
        form = ChildLoginForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            try:
                family = Family.objects.get(family_username=f['family_username'])
                if family.easy_password == f['family_easy_password']:
                    family_username = f['family_username'] 
                    family_name = family.family_name
                    request.session['family_username'] = family_username
                    request.session['family_name'] = family_name
                    return redirect('task-display')
            except Exception as e:
                ''' handle exception with error msg '''
                form = ChildLoginForm()
                return render(request, 'child_login.html', {'form': form, 'error': 'Login error, check your credentials'})
    else:
        form = ChildLoginForm()

    return render(request, 'child_login.html', {'form': form})

@require_http_methods(["GET"])
def display_task(request):
    family_name = request.session.get('family_name')
    family_username = request.session.get('family_username')
    qf = Q(family_username=family_username)
    family = Family.objects.get(qf)
    existing_tasks = [t for t in Task.objects.filter(task_family=family)]
    return render(request, 'task_display.html', {'family': family_name, 'tasks': existing_tasks})

@require_http_methods(["GET"])
def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task is not None:
        task.task_complete = True
        task.save()
    return redirect('task-display')

@require_http_methods(["GET"])
def delete_complete(request):
    Task.objects.filter(task_complete__exact=True).delete()
    return redirect('task-add')

@require_http_methods(["GET", "POST"])
def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        taskform = TaskAddForm(request.POST)
        if taskform.is_valid():
            f = taskform.cleaned_data
            family = task.task_family
            child = Child.objects.get(child_family = family, child_name = f['task_child'])
            task.task_name = f['task_name']
            task.task_importance = f['task_importance']
            task.task_reward = f['task_reward']
            task.task_due = f['task_due']
            task.task_child = child
            if task is not None:
                task.save()
            return redirect('task-add')
    else:
        child_form = ChildAddForm()
        family_name = request.session.get('family_name')
        family_username = request.session.get('family_username')
        parent_name = request.session.get('parent_name')
        family = Family.objects.get(family_username=family_username)
        family_kids = [(c.child_name, c.child_name) for c in Child.objects.filter(child_family=family)] 
        existing_tasks = [t for t in Task.objects.filter(task_family=family) if t != task]
        task_form = TaskAddForm(initial={'task_name': task.task_name,
                                         'task_importance':task.task_importance,
                                         'task_reward': task.task_reward,
                                         'task_due': task.task_due,
                                         'task_child': task.task_child})
        task_form.fields['task_child'].choices = family_kids
        return render(request, 'task_add.html',
                {'task_form': task_form, 'child_form': child_form, 
                 'family': family_name, 'parent': parent_name,
                 'tasks': existing_tasks})

@require_http_methods(["GET"])
def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('index') 
