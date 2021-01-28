from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'mainapp/index.html')


def gen_passwords(request):
    return render(request, 'mainapp/gen_pass.html')
