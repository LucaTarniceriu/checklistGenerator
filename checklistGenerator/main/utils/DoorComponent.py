

class DoorComponent:
    name = str
    verified = str
    borken = str
    number = int
    code = str
    notes = str

    def __init__(self, name, verified = "yes", broken = "no", number = 1, code = "", notes = ""):
        self.name = name
        self.verified = verified
        self.broken = broken
        self.number = number
        self.code = code
        self.notes = notes

    def __repr__(self):
        return "\n" + self.name + " | " + self.verified + " | " + self.verified + " | " + str(self.number) + " |" + self.notes