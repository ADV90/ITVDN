from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def lesson_1_1(request):
    return HttpResponse('<p>Hello World!</p><p>Django is one of the best framework on Python</p><hr>')
