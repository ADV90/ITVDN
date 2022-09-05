from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson_1, name='lesson_1'),
]
