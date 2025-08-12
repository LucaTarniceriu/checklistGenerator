from openpyxl import Workbook, load_workbook
from main.utils.DoorComponent import DoorComponent

class Door:
    site = str

    productType = str
    nrComponente = int

    produs = str
    anFabricatie = int
    nr = str
    dimensiuni = str
    tip = str

    titluTabel = str

    componente = []

    @staticmethod
    def reset(productType):
        wb = load_workbook(filename="xlsx/" + productType + ".xlsx")
        ws = wb.active
        ws['E1'] = "....."
        ws['D2'] = "....."
        ws['D3'] = "....."
        ws['D4'] = "....."
        ws['D5'] = "....."
        ws['D6'] = "....."
        ws['D7'] = "....."
        ws['D8'] = ".....x.....mm"
        ws['D9'] = "....."

        ws['B12'] = "PRODUS: ....."
        ws['B47'] = "□"
        ws['B48'] = "□"
        ws['D49'] = "....."
        ws['D50'] = "....."
        ws['D51'] = "....."

    def __init__(self, site = "empty", productType = "empty", produs = "empty", anFabricatie = 0, nr = "empty", dimensiuni = "empty", tip = "empty", titluTabel = "empty"):
        self.site = site

        self.productType = productType
        self.produs = produs
        self.anFabricatie = anFabricatie
        self.nr = nr
        self.dimensiuni = dimensiuni
        self.tip = tip

        self.titluTabel = titluTabel

        numeComponente = []
        wb = 0

        if productType == "1": #Antifoc
            self.nrComponente = 26
            wb = load_workbook(filename="xlsx/Antifoc.xlsx")
        elif productType == "2": #Automata
            self.nrComponente = 22
            wb = load_workbook(filename="xlsx/Automata.xlsx")
        elif productType == "3": #Burduf
            self.nrComponente = 16
            wb = load_workbook(filename="xlsx/Burduf.xlsx")
        elif productType == "4": #Metalica
            self.nrComponente = 14
            wb = load_workbook(filename="xlsx/Metalica.xlsx")
        elif productType == "5": #Rampa
            self.nrComponente = 16
            wb = load_workbook(filename="xlsx/Rampa.xlsx")
        elif productType == "6": #Rapida
            self.nrComponente = 17
            wb = load_workbook(filename="xlsx/Rapida.xlsx")
        elif productType == "7": #Sectionala
            self.nrComponente = 20
            wb = load_workbook(filename="xlsx/Sectionala.xlsx")
        else:
            print("eroare selectare usa")
            wb = load_workbook(filename="xlsx/error.xlsx")

        ws = wb.active



        for row in range(14, 14 + self.nrComponente):
            nume = ws['C' + str(row)].value
            numeComponente.append(ws['C' + str(row)].value )
            # se extrage numele componentelor de verificat (a doua coloana a tabelului)
            self.componente.append(DoorComponent(nume))


    def __repr__(self):
        return self.productType + " " + self.produs + " " + str(self.anFabricatie) + " " + str(self.site)
