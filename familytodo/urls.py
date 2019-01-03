from django.urls import path
from .views import (index,
                    register_family,
                    register_parent,
                    login_parent,
                    login_child,
                    logout,
                    add_task,
                    display_task,
                    complete_task,
                    delete_complete,
                    edit_task,
                    control_panel)

urlpatterns = [
    path('', index, name='index'),
    path('family-register', register_family, name='family-register'),
    path('parent-register', register_parent, name='parent-register'),
    path('parent-login', login_parent, name='parent-login'),
    path('child-login', login_child, name='child-login'),
    path('logout', logout, name='logout'),
    path('task-add', add_task, name='task-add'),
    path('task-display', display_task, name='task-display'),
    path('complete-task/<task_id>', complete_task, name='complete-task'),
    path('delete-completed', delete_complete, name='complete-delete'),
    path('task-edit/<task_id>', edit_task, name='task-edit'),
    path('control-panel', control_panel, name='control-panel'),
]
