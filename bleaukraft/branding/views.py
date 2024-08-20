from django.shortcuts import render

def home(request):
    return render(request, 'branding/home.html')

def landingpage(request):
    return render(request, 'branding/landingpage.html')

def about(request):
    return render(request, 'branding/about.html')

def services(request):
    return render(request, 'branding/services.html')

def contact(request):
    return render(request, 'branding/contact.html')