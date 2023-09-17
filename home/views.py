from django.shortcuts import render

def home(request):

    context = {
        'teste': 'Estamos na home'
    }

    return render(
        request, 
        'home/index.html',
        context,

    )