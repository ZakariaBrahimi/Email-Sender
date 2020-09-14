from django.shortcuts import render

# Create your views here.

def send_email(request):
    context = {}
    return render(request, 'index.html', context)