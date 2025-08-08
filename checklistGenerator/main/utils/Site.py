from main.utils.Door import Door

class Site:
    contract = str
    beneficiar = str
    locatie = str
    nrComanda = str

    doors = []

    def __init__(self, contract, beneficiar, locatie, nrComanda):
        self.contract = contract
        self.beneficiar = beneficiar
        self.locatie = locatie
        self.nrComanda = nrComanda

    def addDoor(self, door):
        self.doors.append(door)

    def __repr__(self):
        return self.beneficiar+" "+self.locatie