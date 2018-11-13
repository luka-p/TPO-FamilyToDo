from django.urls import re_path
from .views import (index,
                    register_family,
                    login_family)

urlpatterns = [
    re_path('', index),
    re_path(r'^register/', register_family),
    re_path(r'^login/', login_family)
]
