from django.shortcuts import render

# Create your views here.


def CookiePolicy(request):
    """ A view to return the page """

    return render(request, 'cookie_policy/cookie-policy.html')
