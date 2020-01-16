class Customer:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.pesel = None
        # self.dateOfBirth = dateOfBirth
        # self.hisBooks = set()

    def toString(self):
        print("customer's name: ", self.first_name, "| customer's surname:", self.last_name, "| pesel:", self.pesel)




