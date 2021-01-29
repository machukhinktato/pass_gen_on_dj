from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    return render(request, 'mainapp/index.html')


def gen_passwords(request):
    chr_list = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        chr_list.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        chr_list.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        chr_list.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    psw = ''
    for x in range(length):
        psw += random.choice(chr_list)

    return render(request, 'mainapp/gen_pass.html', {'psw': psw})


def about(request):
    return render(request, 'mainapp/about.html')
