from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson_11, name='lesson_11'),
]