from django.contrib import admin
from django.urls import path
from .views import (index,
                    register_family,
                    login_family)

urlpatterns = [
    path('', index),
    path('', register_family),
    path('', login_family)
]
