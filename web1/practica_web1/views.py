from django.shortcuts import render


def saludo(request):
    return render(request, 'inicio.html')
# Create your views here.
