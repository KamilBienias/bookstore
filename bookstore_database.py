import customer, book

class BookstoreDatabase:
    def __init__(self):
        self.customers = set()
        self.books = list()

    def toStringDatabase(self):
        print("Customer: ", self.customers, "| book: ", self.books)

