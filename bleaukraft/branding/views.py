from django.shortcuts import render

def home(request):
    return render(request, 'branding/home.html')

""" To delete it later"""
def landingpage1(request):
    return render(request, 'branding/landingpage1.html')

def landingpage(request):
    return render(request, 'branding/landingpage.html')

def about(request):
    return render(request, 'branding/about.html')

def services(request):
    return render(request, 'branding/services.html')

def contact(request):
    return render(request, 'branding/contact.html')

def testimonials(request):
    return render(request, 'branding/testimonials.html')

def timeline(request):
    return render(request, 'branding/timeline.html')
