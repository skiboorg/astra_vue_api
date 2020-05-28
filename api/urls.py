from django.urls import path, include
from . import views

urlpatterns = [
    path("get_types/", views.get_type, name='user_phone'),
    path("get_templates/", views.get_templates, name='get_templates'),
    path("get_template/<uuid>", views.get_template, name='get_template'),
    path("add_to_cart/<uuid>/<token>", views.add_to_cart, name='add_to_cart')

]