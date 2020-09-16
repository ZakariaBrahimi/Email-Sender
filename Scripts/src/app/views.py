from django.shortcuts import render, redirect
from django.core.mail import send_mass_mail, send_mail
from email_sender.settings import EMAIL_HOST_USER
from django.contrib import messages

# Create your views here.

def send_email(request):
    if request.method == 'POST':
        subject        = request.POST['subject']
        recipient_list = request.POST['to_email']
        message        = request.POST['message']
        send_mail(subject,
                  message,
                  EMAIL_HOST_USER,
                  [recipient_list],
                  fail_silently=False)
        messages.success(request, f'email sent to {recipient_list} successfully.')
        return redirect('/')
    else:
        return render(request, 'index.html')

    context = {
        'recipient_list': recipient_list,
        }
    return render(request, 'index.html', context)