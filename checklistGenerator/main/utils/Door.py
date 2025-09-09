from openpyxl import Workbook, load_workbook
from main.utils.DoorComponent import DoorComponent

class Door:
    id = int
    site = str

    productType = str
    fileName = str
    nrComponente = int

    produs = str
    anFabricatie = int
    nr = str
    dimensiuni = str
    tip = str

    titluTabel = str

    nrCanate = str
    model = str

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

    def __init__(self, site = "empty", productType = "empty", produs = "empty", anFabricatie = 0, nr = "empty", dimensiuni = "empty", tip = "empty", titluTabel = "empty", nrCanate = "", model=""):
        self.site = site

        self.productType = productType
        self.produs = produs
        self.anFabricatie = anFabricatie
        self.nr = nr
        self.dimensiuni = dimensiuni
        self.tip = tip

        self.titluTabel = titluTabel

        self.nrCanate = nrCanate
        self.model = model


    def setFileName(self):
        # a se apela dupa setarea atributului "productType"
        if self.productType == "1": #Antifoc
            self.fileName = "xlsx/Antifoc.xlsx"
            self.nrComponente = 26
        elif self.productType == "2": #Automata
            self.fileName = "xlsx/Automata.xlsx"
            self.nrComponente = 22
        elif self.productType == "3": #Burduf
            self.fileName = "xlsx/Burduf.xlsx"
            self.nrComponente = 16
        elif self.productType == "4": #Metalica
            self.fileName = "xlsx/Metalica.xlsx"
            self.nrComponente = 14
        elif self.productType == "5": #Rampa
            self.fileName = "xlsx/Rampa.xlsx"
            self.nrComponente = 16
        elif self.productType == "6": #Rapida
            self.fileName = "xlsx/Rapida.xlsx"
            self.nrComponente = 17
        elif self.productType == "7": #Sectionala
            self.fileName = "xlsx/Sectionala.xlsx"
            self.nrComponente = 20
        else:
            print("eroare selectare usa")


    def setComponents(self):
        # a se apela dupa apelarea "setFileName"
        numeComponente = []
        wb = load_workbook(filename=self.fileName)
        ws = wb.active
        for row in range(14, 14 + self.nrComponente):
            nume = ws['C' + str(row)].value
            numeComponente.append(ws['C' + str(row)].value )
            # se extrage numele componentelor de verificat (a doua coloana a tabelului)
            self.componente.append(DoorComponent(nume, row-13))


    def __repr__(self):
        return self.productType + " " + self.produs + " " + str(self.anFabricatie) + " " + str(self.site)
