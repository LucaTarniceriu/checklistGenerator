from django.shortcuts import render
from main.utils.Door import Door
from main.utils.Site import Site
from main.utils.DoorComponent import DoorComponent
from django.http import HttpResponse
from .forms import *
from .models import SiteModel, DoorModel, DoorComponentModel


# Create your views here.

def home(request):
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

        context['beneficiar'] = beneficiar
        context['locatie'] = locatie
        context['comanda'] = nr_comanda
        context['addDoorForm'] = AddDoorForm()

    return render(request, "magazin.html", context)

def addDoor(request):
    context = {}
    doorObject = Door()

    if request.method == "POST":
        if request.POST.get("formName") == "addDoorForm":
            productType = request.POST.get("tip_usa")

            if productType == "1": #Antifoc
                form = UsaAntifocForm()
                doorObject.produs = "USA ANTIFOC GLISANTA"
                doorObject.titluTabel = "PRODUS: UȘĂ ANTIFOC GLISANTĂ CU "
            if productType == "2": #Automata
                form = UsaAutomataForm()
                doorObject.produs = "USA AUTOMATA "
                doorObject.titluTabel = "PRODUS: USA AUTOMATA CU "
            if productType == "3": #Burduf
                form = BurdufForm()
                doorObject.produs = "BURDUF DE ETANSARE"
                doorObject.titluTabel = "PRODUS: BURDUF DE ETANSARE"
            if productType == "4": #Metalica
                form = UsaMetalicaForm()
                doorObject.produs = "USA METALICA BATANTA"
                doorObject.titluTabel = "PRODUS: USA METALICA BATANTA"
            if productType == "5": #Rampa
                form = RampaForm()
                doorObject.produs = "RAMPA DE INCARCARE"
                doorObject.titluTabel = "PRODUS: RAMPA DE INCARCARE"
            if productType == "6": #Rapida
                form = UsaRapidaForm()
                doorObject.produs = "USA RAPIDA"
                doorObject.titluTabel = "PRODUS: USA RAPIDA"
            if productType == "7": #Sectionala
                form = UsaSectionalaForm()
                doorObject.produs = "USA SECTIONALA CU ACTIONARE ELECTRICA"
                doorObject.titluTabel = "PRODUS: USA SECTIONALA CU ACTIONARE ELECTRICA"

            context['produs'] = doorObject.produs
            context['doorForm'] = form
    print(doorObject.productType)
    if request.method == "POST":
        if request.POST.get("formName") == "doorForm":

            if doorObject.productType == "1":
                nr_canate = request.POST.get('nr_canate')
                if nr_canate == "1":
                    doorObject.titluTabel += "UN CANAT"
                if nr_canate == "2":
                    doorObject.titluTabel += "DOUA CANATE"
            if doorObject.productType == "2":
                nr_canate = request.POST.get('nr_canate')
                if nr_canate == "1":
                    doorObject.titluTabel += "UN CANAT"
                if nr_canate == "2":
                    doorObject.titluTabel += "DOUA CANATE"
                model = request.POST.get('model')
                if model == "1":
                    doorObject.produs += "GEZE"
                if model == "2":
                    doorObject.produs += "DORMA"
            an_fabricatie = request.POST.get('an_fabricatie')
            nr  = request.POST.get('nr')
            dimensiuni = request.POST.get('dimensiuni')
            tip = request.POST.get('tip')

            site = SiteModel.objects.first()

            doorObject.site = site
            doorObject.anFabricatie = an_fabricatie
            doorObject.nr = nr
            doorObject.dimensiuni = dimensiuni
            doorObject.tip = tip

            print(doorObject)
            door = DoorModel.objects.update_or_create(
                productType = doorObject.productType,
                produs = doorObject.produs,
                anFabricatie = doorObject.anFabricatie,
                nr = doorObject.nr,
                dimensiuni = doorObject.dimensiuni,
                tip = doorObject.tip,
                titluTabel = doorObject.titluTabel,
                site = doorObject.site,
                componentNr = doorObject.nrComponente,
            )



    return render(request, "adaugaUsa.html", context)