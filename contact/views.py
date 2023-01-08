from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thank you for your message.\
                             We aim to respond within 24 hours.')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
