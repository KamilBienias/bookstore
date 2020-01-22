import customer


class Book:

    def __init__(self):
        self.title = None
        self.author_name = None
        self.author_surname = None
        self.price = None
        self.buyer_pesel = customer.Customer().pesel  # earlier was self.buyer = customer.Customer()

    def toString(self):
        print(str(self.title) + " " + str(self.author_name) + " " + str(self.author_surname) + " " + str(self.price) + " " + str(self.buyer_pesel))
        # print("title: ", self.title, "| author's name: ", self.author_name, "| author's surname: ", self.author_surname, "| price: ", self.price, "$ | buyer's pesel: ", self.buyer_pesel)  # displays None. Earlier was self.buyer.toString()

