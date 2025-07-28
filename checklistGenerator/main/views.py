from django.shortcuts import render
from main.utils.Door import Door
from django.http import HttpResponse


# Create your views here.

def home(request):
    antifoc = Door("Antifoc", "Usa glisanta rezistenta la foc", "1234", "123", "2000x3000", "idk")
    print("\n" + str(antifoc.componente) + "\n")
    return render(request, "home.html")
