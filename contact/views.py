from django.shortcuts import render
from django.contrib import messages

from .models import Contact
from .forms import ContactForm

def contact(request):
    """ A view to return the contact us message """

    return render(request, 'contact/contact.html')


def add_message(request):
    """ A view to Add a message """
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            title = request.POST['title']
            message = request.POST['message']
            email = request.POST['email']
            messages.success(request, "Successfully added message!")
            
    return render(request, 'home/index.html')

