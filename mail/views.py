from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm

def send_mail(request):
    res = sm(
        subject = 'Subject',
        message = 'Here is the message.',
        from_email = 'manishnhuchhe30@gmail.com',
        recipient_list = ['manishsht30@gmail.com'],
        fail_silently=False,
    )    

    return HttpResponse(f"Email sent to {res} members")