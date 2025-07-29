from django.shortcuts import render
from main.utils.Door import Door
from django.http import HttpResponse
from .forms import SiteForm
from .models import SiteModel, DoorModel, DoorComponentModel


# Create your views here.

def home(request):
    antifoc = Door("Antifoc", "Usa glisanta rezistenta la foc", "1234", "123", "2000x3000", "idk")
    print("\n" + str(antifoc.componente) + "\n")
    return render(request, "home.html")

def revizie(request):
    context = {}
    context['siteForm'] = SiteForm()

    if request.method == "POST":

        contract = request.POST.get("contract")
        beneficiar = request.POST.get("beneficiar")
        locatie = request.POST.get("locatie")
        nr_comanda = request.POST.get("nr_comanda")

        print(contract, beneficiar, locatie, nr_comanda)

        site = SiteModel.objects.update_or_create(
            contract = contract,
            beneficiar = beneficiar,
            locatie = locatie,
            nrComanda = nr_comanda
        )


    return render(request, "revizie.html", context)