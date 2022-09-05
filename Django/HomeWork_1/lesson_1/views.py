from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def lesson_1(request):
    return HttpResponse('<p>Test</p><hr>')
