# contactapp/views.py
from django.shortcuts import render, redirect
#from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .forms import ContactForm
from django.conf import settings
from datetime import datetime
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
           
           
             # Prepare the HTML message using a template
            email_subject = f"New message from {name}: {subject}"
            html_message = render_to_string('example/contact_email_template.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            })

            # Prepare a plain text version for email fallback
            plain_message = f"Message from {name} ({email}):\n\n{message}"

            # Create the EmailMultiAlternatives object
            email = EmailMultiAlternatives(
                subject=email_subject,
                body=plain_message,  # Plain text message
                from_email=email,  # From email address
                to=[settings.CONTACT_EMAIL,email],  # To email address
            )

            # Attach the HTML version of the email
            email.attach_alternative(html_message, "text/html")  # Attach HTML alternative

            # Send the email
            email.send(fail_silently=False)
            
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'example/lets_talk.html', {'form': form})
   
def success_view(request):
    return render(request, 'example/success_view.html')

   



