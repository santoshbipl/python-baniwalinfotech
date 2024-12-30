# example/views.py

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'example/home.html')


def services(request):
    return render(request, 'example/services.html')


def industries(request):
    return render(request, 'example/industries.html')



def technologies(request):
    return render(request, 'example/technologies.html')



def company(request):
    return render(request, 'example/company.html')


def work(request):
    #return HttpResponse("Original response")

    return render(request, 'example/work.html')


def clients(request):
    return render(request, 'example/clients.html')

def blog(request):
    return render(request, 'example/blog.html')



def contact_us(request):
    return render(request, 'example/contact_us.html')
    
def about_us(request):
    return render(request, 'example/about_us.html')

def lets_talk(request):
    return render(request, 'example/lets_talk.html')



