from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('This is Home Page!')

def about(request):
    return HttpResponse('This is About Page!')

def work(request):
    return HttpResponse('This is Work Page!')

def experience(request):
    return HttpResponse('This is Experience Page!')

def contact(request):
    return HttpResponse('This is Contact Page!')
