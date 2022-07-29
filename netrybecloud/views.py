from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "netrybe/index.html" , {})

def about(request):
    return render(request,"netrybe/about.html",{})

def training(request):
        return render(request, "netrybe/courses.html",{})

def coursesdet(request):
    return render(request, "netrybe/coursesdetails.html",{})

def datasci(request):
    return render(request, "netrybe/datasci.html",{})

def frontend(request):
    return render(request, "netrybe/frontend.html",{})

def productdesign(request):
    return render(request,"netrybe/uiux.html", {})


def contact(request):
    return render(request,"nnetrybe/contact.html", {})

def backend(request):
    return render(request,"netrybe/backend.html", {})


def schprog(request):
    return render(request, "netrybe/schprog.html", {})