from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {"v1": "This is Django Game",
               "v2": "Play game very well",
               'note': "This is useful for send data from model or you can say from the database"
               }
    return render(request, "index.html", context)  # return HttpResponse("This is home page by AG")


def about(request):
    return render(request, "about.html")
    # return HttpResponse("This is about page by AG")


def services(request):
    return render(request, "services.html")
    # return HttpResponse("This is services page by AG")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, "contact.html")
    # return HttpResponse("This is contact page by AG")


def fun(request):
    return render(request, "fun.html")
    # return HttpResponse("This is contact page by AG")
