""" branding views """

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """
    Handles the contact form submission.

    If the request method is POST, it validates the form data and sends an
    email to the admin if the form is valid. If the form is invalid, it
    renders the contact page again with the form errors.

    If the request method is GET, it renders the contact page with an empty
    form.
    """
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
    """
    Renders the contact success page.
    """
    return render(request, 'branding/contact_success.html')


def landingpage(request):
    """
    Renders the landing page.
    """
    return render(request, 'branding/landingpage.html')


def about(request):
    """
    Renders the about page.
    """
    return render(request, 'branding/about.html')


def services(request):
    """
    Renders the services page.
    """
    return render(request, 'branding/services.html')


def terms_of_service(request):
    """
    Renders the terms of service page.
    """
    return render(request, 'branding/terms.html')
