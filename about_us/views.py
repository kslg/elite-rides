from django.shortcuts import render

# Create your views here.


def AboutUs(request):
    """ A view to return the about page """

    return render(request, 'about_us/about-us.html')
