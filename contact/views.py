from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """

    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            title = request.POST.get('title', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            created_at = request.POST.get('created_at', '')

            
            
            context = {
                'name': name,
                'title': title,
                'email': email,
                'message': message,
                'created_at': created_at,
            }
    else:
        contact_form = ContactForm()
        context = {
            'contact_form': contact_form
        }
    
    template = 'contact/contact.html'

    return render(request, template, context)


def add_contact_message(request):
    """ Create a message to send to store owner  """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save('message')
            messages.success(request, "Thank you for contacting us.")
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add message. \
                Please ensure the form is valid')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
