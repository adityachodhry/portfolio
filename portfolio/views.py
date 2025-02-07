from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    contex = {
        'name': 'Aditya Choudhary',
        'age': 24,
        'city': 'Indore'
    }
    # return render(request, 'home.html', contex)
    # # return HttpResponse("This is the home page!")

def home(request):
    return render(request, 'home.html')
    # return HttpResponse("This is the About Page!")

def projects(request):
    return render(request, 'projects.html')
    # return HttpResponse("This is the Projects Page!")

def experience(request):
    return render(request, 'experience.html')
    # return HttpResponse("This is the Experience Page!")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is the Contact Page!")

def blog(request):
    return render(request, 'blog.html')
    # return HttpResponse("This is the Blog Page!")
