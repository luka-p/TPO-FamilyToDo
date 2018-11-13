from django.urls import path
from .views import (index,
                    register_family,
                    login_parent,
                    login_child,
                    add_task)

urlpatterns = [
    path('', index),
    path('family-register', register_family),
    path('parent-login', login_parent),
    path('child-login', login_child),
    path('task-add', add_task),
]
