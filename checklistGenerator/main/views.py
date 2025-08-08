from django.shortcuts import render
from main.utils.Door import Door
from main.utils.Site import Site
from main.utils.DoorComponent import DoorComponent
from django.http import HttpResponse
from .forms import *
from .models import SiteModel, DoorModel, DoorComponentModel


# Create your views here.

def home(request):
    antifoc = Door("Antifoc", "Usa glisanta rezistenta la foc", "1234", "123", "2000x3000", "idk")
    print("\n" + str(antifoc.componente) + "\n")
    return render(request, "home.html")

def revizie(request):
    context = {}
    context['siteForm'] = SiteForm()


    return render(request, "revizie.html", context)

def magazin(request):
    context = {}

    if request.method == "POST":

        contract = request.POST.get("contract")
        beneficiar = request.POST.get("beneficiar")
        locatie = request.POST.get("locatie")
        nr_comanda = request.POST.get("nr_comanda")

        print(contract, beneficiar, locatie, nr_comanda)

        siteObject = Site(contract, beneficiar, locatie, nr_comanda)
        site = SiteModel.objects.update_or_create(
            contract = contract,
            beneficiar = beneficiar,
            locatie = locatie,
            nrComanda = nr_comanda
        )

        print(site)

        context['beneficiar'] = beneficiar
        context['locatie'] = locatie
        context['comanda'] = nr_comanda
        context['addDoorForm'] = AddDoorForm()

    return render(request, "magazin.html", context)

def addDoor(request):
    context = {}

    if request.method == "POST":
        productType = request.POST.get("tip_usa")
        print(productType)

        if productType == "1": #Antifoc
            form = UsaAntifocForm()
            produs = "USA ANTIFOC GLISANTA"
            titluTabel = "PRODUS: UȘĂ ANTIFOC GLISANTĂ CU "
        if productType == "2": #Automata
            form = UsaAutomataForm()
            produs = "USA AUTOMATA "
            titluTabel = "PRODUS: USA AUTOMATA CU "
        if productType == "3": #Burduf
            form = BurdufForm()
            produs = "BURDUF DE ETANSARE"
            titluTabel = "PRODUS: BURDUF DE ETANSARE"
        if productType == "4": #Metalica
            form = UsaMetalicaForm()
            produs = "USA METALICA BATANTA"
            titluTabel = "PRODUS: USA METALICA BATANTA"
        if productType == "5": #Rampa
            form = RampaForm()
            produs = "RAMPA DE INCARCARE"
            titluTabel = "PRODUS: RAMPA DE INCARCARE"
        if productType == "6": #Rapida
            form = UsaRapidaForm()
            produs = "USA RAPIDA"
            titluTabel = "PRODUS: USA RAPIDA"
        if productType == "7": #Sectionala
            form = UsaSectionalaForm()
            produs = "USA SECTIONALA CU ACTIONARE ELECTRICA"
            titluTabel = "PRODUS: USA SECTIONALA CU ACTIONARE ELECTRICA"

        context['produs'] = produs
        context['doorForm'] = form

        if request.method == "POST":
            if productType == "1":
                nr_canate = request.POST.get('nr_canate')
                if nr_canate == "1":
                    titluTabel += "UN CANAT"
                if nr_canate == "2":
                    titluTabel += "DOUA CANATE"
            if productType == "2":
                nr_canate = request.POST.get('nr_canate')
                if nr_canate == "1":
                    titluTabel += "UN CANAT"
                if nr_canate == "2":
                    titluTabel += "DOUA CANATE"
                model = request.POST.get('model')
                if model == "1":
                    produs += "GEZE"
                if model == "2":
                    produs += "DORMA"
            an_fabricatie = request.POST.get('an_fabricatie')
            nr  = request.POST.get('nr')
            dimensiuni = request.POST.get('dimensiuni')
            tip = request.POST.get('tip')

            doorObject = Door(productType, produs, an_fabricatie, nr, dimensiuni, tip, titluTabel)
            door = SiteModel.objects.update_or_create(
                productType = doorObject.productType,
                produs = doorObject.produs,
                anFabricatie = doorObject.anFabricatie,
                nr = doorObject.nr,
                dimensiuni = doorObject.dimensiuni,
                tip = doorObject.tip,
                titluTabel = doorObject.titluTabel,
                # site =
            )



    return render(request, "adaugaUsa.html", context)