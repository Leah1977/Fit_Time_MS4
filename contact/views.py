from django.shortcuts import render


def contact(request):
    """ A view to return the contact page """

    return render(request, 'contact/contact.html')


def add_contact_message(request):
    """ Create a message to send to store owner  """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save()
            messages.success(request, "Successfully added message!")
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
