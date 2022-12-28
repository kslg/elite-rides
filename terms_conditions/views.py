from django.shortcuts import render

# Create your views here.


def TermsConditions(request):
    """ A view to return the page """

    return render(request, 'terms_conditions/terms-conditions.html')
