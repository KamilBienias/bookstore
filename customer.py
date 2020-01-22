class Customer:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.pesel = None
        # self.all_details = str(self.first_name) + " " + str(self.last_name) + " " + str(self.pesel)
        # self.dateOfBirth = dateOfBirth
        # self.hisBooks = set()

    def toString(self):
        print(str(self.first_name) + " " + str(self.last_name) + " " + str(self.pesel))
        # print("customer's name: ", self.first_name, "| customer's surname:", self.last_name, "| pesel:", self.pesel)
        # self.all_details



