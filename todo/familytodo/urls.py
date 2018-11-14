from django.urls import path
from .views import (index,
                    register_family,
                    login_parent,
                    login_child,
                    add_task)

urlpatterns = [
    path('', index),
    path('family-register', register_family, name='family-register'),
    path('parent-login', login_parent, name=parent-login),
    path('child-login', login_child, name='child-login'),
    path('task-add', add_task, name='task-add'),
]
