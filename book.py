import customer


class Book:

    def __init__(self):
        self.title = None
        self.author_name = None
        self.author_surname = None
        self.price = None
        self.buyer = customer.Customer()

    def toString(self):
        print("title: ", self.title, "| author's name: ", self.author_name, "| author's surname: ", self.author_surname, "| price: ", self.price, "$ | buyer: ", self.buyer.toString())  # displays None

