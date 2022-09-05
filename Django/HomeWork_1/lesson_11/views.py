from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def lesson_11(request):
    return HttpResponse('<p>Hello World!</p>')
