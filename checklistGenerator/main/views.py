from django.shortcuts import render, redirect
from main.utils.Door import Door
from main.utils.Site import Site
from main.utils.DoorComponent import DoorComponent
from django.http import HttpResponse
from .forms import *
from .models import SiteModel, DoorModel, DoorComponentModel


# Create your views here.

def home(request):
    request.session['currentSite'] = "empty"
    print(request.session["currentSite"])

    context = {}
    context['siteExists'] = 'false'
    if SiteModel.objects.count() > 0:
        context['locatiiDatabase'] = SiteModel.objects.all()
        context['siteExists'] = 'true'
    return render(request, "home.html", context)

def revizie(request):
    print(request.session["currentSite"])
    context = {}
    context['siteForm'] = SiteForm()


    return render(request, "revizie.html", context)


def updateTitle(doorId):
    door = DoorModel.objects.get(id=doorId)
    if door.productType == "1":
        nr_canate = door.nrCanate
        if nr_canate == "1":
            door.titluTabel += "UN CANAT"
        if nr_canate == "2":
            door.titluTabel += "DOUA CANATE"
    if door.productType == "2":
        nr_canate = door.nrCanate
        if nr_canate == "1":
            door.titluTabel += "UN CANAT"
        if nr_canate == "2":
            door.titluTabel += "DOUA CANATE"
        model = door.model
        if model == "1":
            door.produs += "GEZE"
        if model == "2":
            door.produs += "DORMA"
    door.save()


def magazin(request):
    print(request.session["currentSite"])
    context = {}

    if request.method == "POST":
        if request.POST.get("formName") == "siteForm":
            contract = request.POST.get("contract")
            beneficiar = request.POST.get("beneficiar")
            locatie = request.POST.get("locatie")
            nr_comanda = request.POST.get("nr_comanda")

            request.session['currentSite'] = locatie

            #siteObject = Site(contract, beneficiar, locatie, nr_comanda)
            SiteModel.objects.update_or_create(
                contract = contract,
                beneficiar = beneficiar,
                locatie = locatie,
                nrComanda = nr_comanda
            )
        else:
            site = SiteModel.objects.get(locatie=request.session['currentSite'])
            (beneficiar, locatie, nr_comanda) = (site.beneficiar, site.locatie, site.nrComanda)

        site = SiteModel.objects.get(locatie=request.session['currentSite'])
        if request.POST.get("formName") == "doorForm":
            doorObject = Door()
            doorObject.productType = request.session.get('productType')

            if doorObject.productType == "1": #Antifoc
                doorObject.nrCanate = request.POST.get('nr_canate')

                doorObject.produs = "USA ANTIFOC GLISANTA"
                doorObject.titluTabel = "PRODUS: UȘĂ ANTIFOC GLISANTĂ CU "
            if doorObject.productType == "2": #Automata
                doorObject.nrCanate = request.POST.get('nr_canate')
                doorObject.model = request.POST.get('model')

                doorObject.produs = "USA AUTOMATA "
                doorObject.titluTabel = "PRODUS: USA AUTOMATA CU "
            if doorObject.productType == "3": #Burduf
                doorObject.produs = "BURDUF DE ETANSARE"
                doorObject.titluTabel = "PRODUS: BURDUF DE ETANSARE"
            if doorObject.productType == "4": #Metalica
                doorObject.produs = "USA METALICA BATANTA"
                doorObject.titluTabel = "PRODUS: USA METALICA BATANTA"
            if doorObject.productType == "5": #Rampa
                doorObject.produs = "RAMPA DE INCARCARE"
                doorObject.titluTabel = "PRODUS: RAMPA DE INCARCARE"
            if doorObject.productType == "6": #Rapida
                doorObject.produs = "USA RAPIDA"
                doorObject.titluTabel = "PRODUS: USA RAPIDA"
            if doorObject.productType == "7": #Sectionala
                doorObject.produs = "USA SECTIONALA CU ACTIONARE ELECTRICA"
                doorObject.titluTabel = "PRODUS: USA SECTIONALA CU ACTIONARE ELECTRICA"

            an_fabricatie = request.POST.get('an_fabricatie')
            nr = request.POST.get('nr')
            dimensiuni = request.POST.get('dimensiuni')
            tip = request.POST.get('tip')


            doorObject.site = site
            doorObject.anFabricatie = an_fabricatie
            doorObject.nr = nr
            doorObject.dimensiuni = dimensiuni
            doorObject.tip = tip

            doorObject.setFileName()
            doorObject.setComponents()

            print("doorObject=", doorObject)

            if request.POST.get('id') != "empty": # already in database. Will be updated not created
                doorId = request.POST.get('id')
                print("doorId", doorId, "; editing database")
                print(request.session)
                door = DoorModel.objects.get(id=int(doorId))
                door.site = doorObject.site
                door.productType = doorObject.productType
                door.produs = doorObject.produs
                door.anFabricatie = doorObject.anFabricatie
                door.nr = doorObject.nr
                door.dimensiuni = doorObject.dimensiuni
                door.tip = doorObject.tip
                door.titluTabel = doorObject.titluTabel
                door.componentNr = doorObject.nrComponente
                door.nrCanate = doorObject.nrCanate
                door.model = doorObject.model
                door.save()

                componentsToEdit = DoorComponentModel.objects.filter(door=door)
                for entry in componentsToEdit:
                    componentNrCrt = entry.nrcrt
                    if request.POST.get('verified_'+str(componentNrCrt)+'_'+str(door.id)) == 'on':
                        entry.verified = True
                    else:
                        entry.verified = False
                    if request.POST.get('broken_'+str(componentNrCrt)+'_'+str(door.id)) == 'on':
                        entry.broken = True
                    else:
                        entry.broken = False
                    entry.number = request.POST.get('number_'+str(componentNrCrt)+'_'+str(door.id))
                    entry.notes = request.POST.get('notes_'+str(componentNrCrt)+'_'+str(door.id))

                    entry.save()


            else: # not in database. Create entry
                doorEntry = DoorModel.objects.update_or_create(
                    site=doorObject.site,
                    productType=doorObject.productType,
                    produs=doorObject.produs,
                    anFabricatie=doorObject.anFabricatie,
                    nr=doorObject.nr,
                    dimensiuni=doorObject.dimensiuni,
                    tip=doorObject.tip,
                    titluTabel=doorObject.titluTabel,
                    componentNr=doorObject.nrComponente,

                    nrCanate=doorObject.nrCanate,
                    model=doorObject.model
                )

                for component in doorObject.componente:
                    print(component)
                    componentEntry = DoorComponentModel.objects.update_or_create(
                        door=doorEntry[0],
                        name=component.name,
                        number=component.number,
                        notes=component.notes,
                        nrcrt=component.nrcrt,
                    )

        context['beneficiar'] = beneficiar
        context['locatie'] = locatie
        context['comanda'] = nr_comanda
        context['addDoorForm'] = AddDoorForm()

    site = SiteModel.objects.get(locatie=request.session['currentSite'])
    context['doorDatabase'] = DoorModel.objects.filter(site=site)

    return render(request, "magazin.html", context)

def addDoor(request):
    context = {}

    if request.method == "POST":
        if request.POST.get("formName") == "addDoorForm":
            productType = request.POST.get("tip_usa")
            request.session['productType'] = productType

            context["source"] = "from_add"

            if productType == "1": #Antifoc
                form = UsaAntifocForm()
                produs = "Antifoc"
            if productType == "2": #Automata
                form = UsaAutomataForm()
                produs="Automata"
            if productType == "3": #Burduf
                form = BurdufForm()
                produs = "Burduf"
            if productType == "4": #Metalica
                form = UsaMetalicaForm()
                produs = "Metalica"
            if productType == "5": #Rampa
                form = RampaForm()
                produs = "Rampa"
            if productType == "6": #Rapida
                form = UsaRapidaForm()
                produs = "Rapida"
            if productType == "7": #Sectionala
                form = UsaSectionalaForm()
                produs = "Sectionala"

            context['productType'] = productType
            context['produs'] = produs
            context['doorForm'] = form

        if request.POST.get("formName") == "doorEntryId":
            doorId = request.POST.get('id')
            door = DoorModel.objects.get(id=doorId)
            productType = door.productType
            request.session['productType'] = productType

            context["componentDatabase"] = DoorComponentModel.objects.filter(door=door)
            context["source"] = "from_edit"

## COMPLETE THE FORMS WITH THE DATA IN THE DATABASE, CHANGE NAME AS UPDATE_DATA?
            if productType == "1": #Antifoc
                form = UsaAntifocForm(initial={
                    "nr_canate": door.nrCanate,
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                })
                produs = "Antifoc"
            if productType == "2": #Automata
                form = UsaAutomataForm(initial={
                    "nr_canate": door.nrCanate,
                    "model": door.model,
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                }
                )
                produs="Automata"
            if productType == "3": #Burduf
                form = BurdufForm(initial={
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                })
                produs = "Burduf"
            if productType == "4": #Metalica
                form = UsaMetalicaForm(initial={
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                })
                produs = "Metalica"
            if productType == "5": #Rampa
                form = RampaForm(initial={
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                })
                produs = "Rampa"
            if productType == "6": #Rapida
                form = UsaRapidaForm(initial={
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                })
                produs = "Rapida"
            if productType == "7": #Sectionala
                form = UsaSectionalaForm(initial={
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                })
                produs = "Sectionala"

            context['productType'] = productType
            context['produs'] = produs
            context['doorForm'] = form
        print("type=",productType)





    return render(request, "adaugaUsa.html", context)

def deleteSite(request):
    if request.method == "POST":
        site = SiteModel.objects.filter(locatie=request.POST.get('location').strip())
        site.delete()
    return redirect('home')

def magazinRedirect(request):
    context = {}


    if request.method == "POST":
        request.session['currentSite'] = request.POST.get("location").strip()

    site = SiteModel.objects.get(locatie=request.session['currentSite'])

    context['doorDatabase'] = DoorModel.objects.filter(site=site)
    context['beneficiar'] = site.beneficiar
    context['locatie'] = site.locatie
    context['comanda'] = site.nrComanda
    context['addDoorForm'] = AddDoorForm()
    return render(request, "magazin.html", context)

def deleteDoor(request):
    if request.method == "POST":
        doorId = request.POST.get('id')
        DoorModel.objects.get(id=doorId).delete()
    return redirect('magazinRedirect')