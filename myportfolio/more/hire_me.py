# hire_me_views.py

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from ..forms import HireMeForm


def hire_me(request):
    if request.method == 'POST':
        form = HireMeForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']
            service_type = form.cleaned_data['service_type']
            duration = form.cleaned_data['duration']
            description = form.cleaned_data['description']
            reference = form.cleaned_data['reference']
            
            # Construct email message
            subject = f'New Hire Me Inquiry from {name}'
            message = f'''
                Name: {name}
                Email: {email}
                Role: {role}
                Project Type: {service_type}
                Duration: {duration}
                Description: {description}
                How Hear About: {reference}
            '''
            # Send email
            send_mail(
                subject,
                message,
                'vdnamitesh@example.com',  # Replace with your email
                ['vdnamitesh@example.com'],  # Replace with recipient email
                fail_silently=False,
            )
            # Redirect to a thank you page or homepage after submission
            return HttpResponseRedirect('/thank-you/')  # Replace with your desired URL
    else:
        form = HireMeForm()
    return render(request, 'myportfolio/html/hire_me.html', {'form': form})
