

class DoorComponent:
    name = str
    nrcrt = int
    verified = bool
    borken = bool
    number = int
    code = str
    notes = str

    def __init__(self, name, nrcrt, verified = True, broken = False, number = 1, code = "", notes = ""):
        self.name = name
        self.nrcrt = nrcrt
        self.verified = verified
        self.broken = broken
        self.number = number
        self.code = code
        self.notes = notes

    def __repr__(self):
        return "\n" + self.name + " | " + str(self.nrcrt) + " | " + str(self.verified) + " | " + str(self.broken) + " | " + str(self.number) + " |" + self.notes