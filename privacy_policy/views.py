from django.shortcuts import render

# Create your views here.


def PrivacyPolicy(request):
    """ A view to return the page """

    return render(request, 'privacy_policy/privacy-policy.html')
