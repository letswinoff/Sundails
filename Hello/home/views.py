from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }
    
    return render(request, 'index.html', context)
    # return HttpResponse("this is hompage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
       
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been successfully submitted!')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")


