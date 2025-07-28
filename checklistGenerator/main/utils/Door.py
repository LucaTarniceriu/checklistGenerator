from openpyxl import Workbook, load_workbook
from main.utils.DoorComponent import DoorComponent

class Door:
    productType = str
    nrComponente = int

    produs = str
    anFabricatie = int
    nr = str
    dimensiuni = str
    tip = str

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

    def __init__(self, productType, produs, anFabricatie, nr, dimensiuni, tip):
        self.productType = productType
        self.produs = produs
        self.anFabricatie = anFabricatie
        self.nr = nr
        self.dimensiuni = dimensiuni
        self.tip = tip

        wb = load_workbook(filename="xlsx/" + productType + ".xlsx")
        ws = wb.active

        numeComponente = []
        if productType == "Antifoc":
            self.nrComponente = 26
        elif productType == "Automata":
            self.nrComponente = 10
        elif productType == "Burduf":
            self.nrComponente = 10
        elif productType == "Metalica":
            self.nrComponente = 10
        elif productType == "Rampa":
            self.nrComponente = 10
        elif productType == "Rapida":
            self.nrComponente = 10
        elif productType == "Sectionala":
            self.nrComponente = 10


        for row in range(14, 14 + self.nrComponente):
            nume = ws['C' + str(row)].value
            numeComponente.append(ws['C' + str(row)].value )
            # se extrage numele componentelor de verificat (a doua coloana a tabelului)
            self.componente.append(DoorComponent(nume))

