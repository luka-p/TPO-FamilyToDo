from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo, Family, Kids
from .forms import TodoForm, ParentForm, KidForm, KidAddForm, FamilyForm, Form1FRI, Form2FRI, Form3FRI
import json

def index(request, family):
    todo_list = Todo.objects.order_by('id')

    kid = KidAddForm()
    form = TodoForm()
    kids = Kids.objects.filter(family=family)

    context = {'todo_list' : todo_list, 'form' : form, 'kid': kid, 'family': family, 'kids': kids}

    return render(request, 'todo/index.html', context)

def kids_todo(request, family):
    seznam = Todo.objects.all().values_list('id','text','ime_otroka','nujnost','complete')
    print(seznam)
    todo_list = Todo.objects.order_by('id')

    context = {'todo_list' : todo_list, 'family': family, 'seznam': seznam}

    return render(request, 'todo/todo.html', context)

def home_page(request):
    # ADD FAMILY
    #f = Family(name='druzina1', password='test')
    #f.save()
    print(Family.objects.all())
    return render(request, 'todo/home.html')

@require_POST
def addTodo(request, family):
    form = TodoForm(request.POST)
    kid = KidAddForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'],nujnost=request.POST['importance'],ime_otroka=request.POST['otrok'])
        new_todo.save()

    if kid.is_valid():
        kid_name = request.POST['name']
        k = Kids(family=family, kidname=kid_name)
        k.save()
        #print(kid_name)
        #print(Kids.objects.all())
        #print(Kids.objects.filter(family=family))

    return index(request, family)

def addKid(request):
    return redirect('index')

def parentLogin(request):
    form = ParentForm(request.POST)

    context = {'form': form}

    if 'register' in request.POST:
        if form.is_valid():
            familyusername = request.POST['username']
            password = request.POST['password']
            f = Family(name=familyname, password=fampass)
            f.save()
            print(familyusername)
            print(password)
            return redirect('parentlogin')

    if 'login' in request.POST:
        if form.is_valid():
            familyusername= request.POST['username']
            password = request.POST['password']
            check = Family.objects.get(name=familyusername).get_pass()
            if check == password:
                return index(request, familyusername)

    return render(request, 'todo/parentlogin.html', context)

#@require_POST
def kidLogin(request):
    form = KidForm(request.POST)

    context = {'form': form}

    if form.is_valid():
        familiy = request.POST['username']
        print(familiy)
        if Family.objects.filter(name=familiy).exists():
            return kids_todo(request, familiy)
        else:
            context['error'] = 'Invalid family name.'

    return render(request, 'todo/kidlogin.html', context)

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('todo', 'druzina1')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index', 'druzina1')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index', 'druzina1')

def f1(request):
    form = Form1FRI(request.POST)
    context = {'form': form}
    if form.is_valid():
        valid = request.POST
        valid_json = json.dumps(valid)
        print(valid_json)
        context = {'form': form.clean(), 'msg': "Hvala za oddano vlogo" }
        return render(request, 'todo/f1.html', context)
    return render(request, 'todo/f1.html', context)


def f2(request):
    form = Form2FRI(request.POST)
    context = {'form': form}
    if form.is_valid():
        valid = request.POST
        valid_json = json.dumps(valid)
        print(valid_json)
        context = {'form': form.clean(), 'msg': "Hvala za oddano vlogo" }
        return render(request, 'todo/f2.html', context)
    return render(request, 'todo/f2.html', context)

def f3(request):
    form = Form3FRI(request.POST)
    context = {'form': form}
    if form.is_valid():
        print("Valid")
        valid = request.POST
        valid_json = json.dumps(valid)
        print(valid_json)
        context = {'form': form.clean(), 'msg': "Hvala za oddano vlogo" }
        return render(request, 'todo/f3.html', context)
    return render(request, 'todo/f3.html', context)
