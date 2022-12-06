from django.shortcuts import render

# Create your views here.

def servicing(request):
    """ A view to return the servicing page """

    return render(request, 'servicing/servicing.html')
