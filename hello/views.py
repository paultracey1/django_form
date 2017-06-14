from django.shortcuts import render
from .models import Contact

def say_hello(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts_list': contacts})

def add_contact(request):
    if request.method == "POST":
        return render(request, 'contactadded.html')
    else:
        return render(request, 'add.html')

