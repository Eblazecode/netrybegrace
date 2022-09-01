from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "netrybe/index.html" , {})

def about(request):
    return render(request,"netrybe/about.html",{})

def training(request):
        return render(request, "netrybe/courses.html",{})

def coursesdetails(request):
    return render(request, "netrybe/coursesdetails.html",{})

def datasci(request):
    return render(request, "netrybe/datasci.html",{})

def frontend(request):
    return render(request, "netrybe/frontend.html",{})

def productdesign(request):
    return render(request,"netrybe/uiux.html", {})


def contact(request):
    return render(request,"netrybe/contact.html", {})

def backend(request):
    return render(request,"netrybe/backend.html", {})


def nimbly(request):
    return render(request,"netrybe/nimblyprogram.html", {})


def schprog(request):
    return render(request, "netrybe/schprog.html", {})
    
def aftersch(request):
    return render(request, "netrybe/afterschool.html", {})

def workshop(request):
    return render(request, "netrybe/workshop.html", {})
def software(request):
    return render(request, "netrybe/softwaredev.html", {})

def business(request):
    return render(request, "netrybe/businessint.html", {})

def entreprise(request):
    return render(request, "netrybe/enterprise.html", {})

def entreprise(request):
    return render(request, "netrybe/hustlebiz.html", {})