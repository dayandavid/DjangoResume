from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    message = _('Hello World')
    
    return render(request, 'DjangoTestingApp/index.html', {'helloWorld': message})
