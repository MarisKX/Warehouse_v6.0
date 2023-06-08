from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from companies.models import Company
# from .models import AppSettings


# Index (home) view
def index(request):
    """ A view to return the index page """
    context = {
    }

    return render(request, 'home/index.html', context)
