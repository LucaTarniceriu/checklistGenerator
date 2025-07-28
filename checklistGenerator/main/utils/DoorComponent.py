

class DoorComponent:
    name = str
    status = str
    number = int
    notes = str

    def __init__(self, name, status = "OK", number = 1, notes = ""):
        self.name = name
        self.status = status
        self.number = number
        self.notes = notes

    def __repr__(self):
        return "\n" + self.name + " | " + self.status + " | " + str(self.number) + " |" + self.notes