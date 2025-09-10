from django.shortcuts import render, redirect
from django.utils.translation.trans_real import language_code_re

from main.utils.Door import Door
from main.utils.Site import Site
from main.utils.DoorComponent import DoorComponent
from django.http import HttpResponse
from .forms import *
from .models import SiteModel, DoorModel, DoorComponentModel

import os, webbrowser
from pypdf import PdfWriter


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

def updateTitle(doorObject):
    if doorObject.productType == "1":
        nr_canate = doorObject.nrCanate
        if nr_canate == "1":
            doorObject.titluTabel += " UN CANAT"
        if nr_canate == "2":
            doorObject.titluTabel += " DOUA CANATE"
    if doorObject.productType == "2":
        nr_canate = doorObject.nrCanate
        if nr_canate == "1":
            doorObject.titluTabel += " UN CANAT"
        if nr_canate == "2":
            doorObject.titluTabel += " DOUA CANATE"
        model = doorObject.model
        if model == "1":
            doorObject.produs += " GEZE"
        if model == "2":
            doorObject.produs += " DORMA"


def magazin(request):
    DOOR_FORMS = {
        "1": UsaAntifocForm,
        "2": UsaAutomataForm,
        "3": BurdufForm,
        "4": UsaMetalicaForm,
        "5": RampaForm,
        "6": UsaRapidaForm,
        "7": UsaSectionalaForm,
    }
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


        site = SiteModel.objects.get(locatie=request.session['currentSite'])
        (beneficiar, locatie, nr_comanda) = (site.beneficiar, site.locatie, site.nrComanda)
        if request.POST.get("formName") == "doorForm":
            doorObject = Door()
            doorObject.productType = request.session.get('productType')

            FormClass = DOOR_FORMS.get(doorObject.productType)
            form = FormClass(request.POST)
            if form.is_valid():

                if doorObject.productType == "1": #Antifoc
                    doorObject.nrCanate = form.cleaned_data['nr_canate']

                    doorObject.produs = "USA ANTIFOC GLISANTA"
                    doorObject.titluTabel = "PRODUS: UȘĂ ANTIFOC GLISANTĂ CU"
                if doorObject.productType == "2": #Automata
                    doorObject.nrCanate = form.cleaned_data['nr_canate']
                    doorObject.model = form.cleaned_data['model']

                    doorObject.produs = "USA AUTOMATA"
                    doorObject.titluTabel = "PRODUS: USA AUTOMATA CU"
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

                an_fabricatie = form.cleaned_data['an_fabricatie']
                nr = form.cleaned_data['nr']
                dimensiuni = form.cleaned_data['dimensiuni']
                tip = form.cleaned_data['tip']
                data_inspectiei = form.cleaned_data['data_inspectiei']
                tehnician = form.cleaned_data['tehnician']
                oras = form.cleaned_data['oras']


                doorObject.site = site
                doorObject.anFabricatie = an_fabricatie
                doorObject.nr = nr
                doorObject.dimensiuni = dimensiuni
                doorObject.tip = tip
                doorObject.data_inspectiei = data_inspectiei
                doorObject.tehnician = tehnician
                doorObject.oras = oras

                doorObject.setFileName()
                doorObject.setComponents()

                print("doorObject=", doorObject)

                if request.POST.get('id') != "empty": # already in database. Will be updated not created
                    doorId = int(form.cleaned_data['id'])
                    print("doorId", doorId, ";editing database")
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
                    door.dataInspectiei = doorObject.data_inspectiei
                    door.tehnician = doorObject.tehnician
                    door.oras = doorObject.oras
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
                        model=doorObject.model,
                        dataInspectiei=doorObject.data_inspectiei,
                        tehnician=doorObject.tehnician,
                        oras=doorObject.oras,
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
                    "data_inspectiei": door.dataInspectiei,
                    "tehnician": door.tehnician,
                    "oras": door.oras,
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
                    "data_inspectiei": door.dataInspectiei,
                    "tehnician": door.tehnician,
                    "oras": door.oras,
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
                    "data_inspectiei": door.dataInspectiei,
                    "tehnician": door.tehnician,
                    "oras": door.oras,
                })
                produs = "Burduf"
            if productType == "4": #Metalica
                form = UsaMetalicaForm(initial={
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                    "data_inspectiei": door.dataInspectiei,
                    "tehnician": door.tehnician,
                    "oras": door.oras,
                })
                produs = "Metalica"
            if productType == "5": #Rampa
                form = RampaForm(initial={
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                    "data_inspectiei": door.dataInspectiei,
                    "tehnician": door.tehnician,
                    "oras": door.oras,
                })
                produs = "Rampa"
            if productType == "6": #Rapida
                form = UsaRapidaForm(initial={
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                    "data_inspectiei": door.dataInspectiei,
                    "tehnician": door.tehnician,
                    "oras": door.oras,
                })
                produs = "Rapida"
            if productType == "7": #Sectionala
                form = UsaSectionalaForm(initial={
                    "an_fabricatie": door.anFabricatie,
                    "nr": door.nr,
                    "dimensiuni": door.dimensiuni,
                    "tip": door.tip,
                    "id": str(doorId),
                    "data_inspectiei": door.dataInspectiei,
                    "tehnician": door.tehnician,
                    "oras": door.oras,
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

def export(request):
    # Site.fillFile("Antifoc.xlsx", "123456789", "Antifoc", "LIDL", "246", 2024, "62066710", 1, "1000x1000mm", "UȘĂ ANTIFOC GLISANTĂ CU UN CANAT", "10.09.2025", "Teofil Tarniceriu", "Timisoara", tip="culisanta")

    location = request.POST.get('location')
    site = SiteModel.objects.get(locatie=location)
    doorDB = DoorModel.objects.filter(site=site)

    doorCount = 0
    for doorEntry in doorDB: # to export the files with correct title
        doorCount = doorCount + 1
        doorObject = Door(site, doorEntry.productType, doorEntry.produs, doorEntry.anFabricatie, doorEntry.nr, doorEntry.dimensiuni, doorEntry.tip, doorEntry.titluTabel, doorEntry.nrCanate, doorEntry.model, doorEntry.dataInspectiei, doorEntry.tehnician, doorEntry.oras)
        updateTitle(doorObject)
        doorObject.setFileName()
        doorObject.setComponents()

        for component in doorObject.componente:
            componentEntry = DoorComponentModel.objects.get(door=doorEntry,nrcrt=component.nrcrt)
            component.verified = componentEntry.verified
            component.broken = componentEntry.broken
            component.number = componentEntry.number
            component.notes = componentEntry.notes

        siteObject = Site(site.contract, site.beneficiar, site.locatie, site.nrComanda)

        Site.fillFile(siteObject, doorObject, doorCount)

    pdfs = os.listdir(Site.output_dir)
    resultName = os.path.basename(pdfs[0]).split("(")[0]
    merger = PdfWriter()
    print(os.path.join(Site.final_output_dir, resultName + ".pdf"))
    for pdf in pdfs:
        merger.append(os.path.join(Site.output_dir, pdf))
        os.remove(os.path.join(Site.output_dir, pdf))
    merger.write(os.path.join(Site.final_output_dir, resultName + ".pdf"))
    merger.close()



    print("pdf files:", pdfs)
    print(os.path.join(Site.output_dir, resultName))
    webbrowser.open_new(os.path.join(Site.final_output_dir, resultName + ".pdf"))
    return redirect('home')