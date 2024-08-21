""" branding views """
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=message,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )

            # Redirect to success page
            return redirect('branding:contact_success')
    else:
        form = ContactForm()

    return render(request, 'branding/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'branding/contact_success.html')


def home(request):
    return render(request, 'branding/home.html')

def landingpage(request):
    return render(request, 'branding/landingpage.html')

def about(request):
    return render(request, 'branding/about.html')

def services(request):
    return render(request, 'branding/services.html')

def terms_of_service(request):
    return render(request, 'branding/terms.html')
