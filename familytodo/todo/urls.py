from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('tasks/<family>', views.index, name='index'),
    path('todo/<family>', views.kids_todo, name='todo'),
    path('add/<family>', views.addTodo, name='add'),
    path('addkid', views.addKid, name='addkid'),
    path('parentLogin', views.parentLogin, name='parentlogin'),
    path('kidLogin', views.kidLogin, name='kidlogin'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('f1', views.f1, name='f1'),
    path('f2', views.f2, name='f2'),
    path('f3', views.f3, name='f3')
]
