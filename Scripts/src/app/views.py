from django.shortcuts import render, redirect
from django.core.mail import send_mass_mail, send_mail,EmailMessage
from email_sender.settings import EMAIL_HOST_USER,EMAIL_BACKEND
from django.contrib import messages
from .forms import SubscribeForm

# Create your views here.

def send_email(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            message = form.cleaned_data['body']
            subject = form.cleaned_data['subject']
            to_email = request.POST['to_email']
            attach = form.cleaned_data['attachments']
            email = EmailMessage(subject, message, EMAIL_HOST_USER, to_email)
            email.attach(attach)
            email.send(fail_silently=False)
            return redirect('https://docs.python.org/3/library/email.mime.html#email.mime.base.MIMEBase')
    else:
        form = SubscribeForm()
    # if request.method == 'POST':
        # subject        = request.POST['subject']
        # recipient_list = request.POST['to_email']
        # message            = request.POST['message']
        # email = EmailMessage(subject,message,EMAIL_HOST_USER, [recipient_list])
        # # word = open("TO DO.docx", 'r')
        # email.attach('https://drive.google.com/file/d/1tNYrastT3PA6Lxd8-u_KDOSG7tkGof0r/view?usp=sharing', 'joiddsc.png')
        # # email.attach_file("Users\Zakaria Abdessamed\Desktop\ZakariaAbdessamedBrahimiResume.pdf", 'application/pdf')
        # email.send(fail_silently=False)
        # return redirect('/')
    context = {
        'form': form,
    }
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