from django.shortcuts import render

def index(request):
    message = 'Hello World Message'
    
    return render(request, 'DjangoTestingApp/index.html', {'helloWorld': message})
