from django.shortcuts import render, redirect
from django.core.mail import send_mass_mail, send_mail,EmailMessage
from email_sender.settings import EMAIL_HOST_USER,EMAIL_BACKEND
from django.contrib import messages

# Create your views here.

def send_email(request):
    if request.method == 'POST':
        subject        = request.POST['subject']
        recipient_list = request.POST['to_email']
        message        = request.POST['message']
        email = EmailMessage(subject,message,EMAIL_HOST_USER, [recipient_list])
        # word = open("TO DO.docx", 'r')
        email.attach('https://drive.google.com/file/d/1tNYrastT3PA6Lxd8-u_KDOSG7tkGof0r/view?usp=sharing', 'joiddsc.png')
        # email.attach_file("Users\Zakaria Abdessamed\Desktop\ZakariaAbdessamedBrahimiResume.pdf", 'application/pdf')
        email.send(fail_silently=False)
        return redirect('/')
    context = {}
    return render(request, 'index.html', context)


# def send_email(request):
#     if request.method == 'POST':
#         
#         subject        = request.POST['subject']
#         recipient_list = request.POST['to_email']
#         message        = request.POST['message']
#         send_mass_mail((subject,
#                   message,
#                   EMAIL_HOST_USER,
#                   [recipient_list]),
#                   fail_silently=False)
#         messages.success(request, f'email sent to {recipient_list} successfully.')
#         # return redirect('/')
#     else:
#         return render(request, 'index.html')

#     context = {
#         'recipient_list': recipient_list,
#         }
#     return render(request, 'index.html', context)