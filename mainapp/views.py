from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    return render(request, 'mainapp/index.html')


def gen_passwords(request):
    chr_list = list('abcdefghijklmnopqrstuvwxyz')
    psw = random.choice(chr_list)
    content = {
        'psw': psw,
    }
    return render(request, 'mainapp/gen_pass.html', content)


def about(request):
    return render(request, 'mainapp/about.html')