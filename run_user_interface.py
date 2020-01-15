import book
import customer
import bookstore_database


class UserInterface:
    def __init__(self, database_object):
        self.database_object = database_object

    def menu(self):
        quit_program = False
        while not quit_program:
            print("Chose number from menu:")
            print("1. Add new customer")
            print("2. Add new book")
            print("3. Show all customers")
            print("4. Show all books")
            print("0. Quit bookstore")
            is_number_error = True
            while is_number_error:
                try:
                    chosen_number = input("Pass number (0 - 4): ")
                    chosen_number_int = int(chosen_number)
                    if chosen_number_int not in [0, 1, 2, 3, 4]:
                        raise NameError()
                    is_number_error = False
                except ValueError as e:
                    print(chosen_number + " is not an integer")
                except NameError as e:
                    print(chosen_number + " is out of menu")

            if chosen_number_int == 1:
                self.add_customer()
            if chosen_number_int == 2:
                self.add_book()
            if chosen_number_int == 3:
                self.all_customers()
            if chosen_number_int == 4:
                self.all_books()
            if chosen_number_int == 0:
                print("Bye bye")
                quit_program = True

    def add_customer(self):
        new_customer = customer.Customer()
        # is_empty = True
        # while is_empty:
        #     passed_first_name = input("Pass new customer's first name: ")
        #     if len(passed_first_name) == 0:
        #         raise ValueError("You should pass new customer's first name")
        #     is_empty = False
        passed_first_name = input("Pass new customer's first name: ")
        new_customer.first_name = passed_first_name
        passed_last_name = input("Pass new customer's last name: ")
        new_customer.last_name = passed_last_name
        print("You have added a new customer: ")
        new_customer.toString()
        # UserInterface.all_customers.add(new_customer)
        self.database_object.customers.add(new_customer)

    def add_book(self):
        new_book = book.Book()
        passed_title = input("Pass new book's title: ")
        new_book.title = passed_title
        passed_autor_name = input("Pass new book's author's name: ")
        new_book.author_name = passed_autor_name
        passed_autor_surname = input("Pass new book's author's surname: ")
        new_book.author_surname = passed_autor_surname

        is_price_error = True
        while is_price_error:
            try:
                passed_price_string = input("Pass new book's price (use a dot instead of a comma): ")
                passed_price = float(passed_price_string)
                passed_price_rounded = round(passed_price, 2)
                is_price_error = False
            except ValueError as e:
                print(passed_price_string + " is not a float number")

        new_book.price = passed_price_rounded
        print("You have added a new book: ")
        new_book.toString()
        self.database_object.books.append(new_book)

    def all_customers(self):
        print("ALL CUSTOMERS:")
        for c in self.database_object.customers:
            c.toString()

    def all_books(self):
        print("ALL BOOKS:")
        for b in self.database_object.books:
            b.toString()


def main():
    database_object = bookstore_database.BookstoreDatabase()
    user_interface = UserInterface(database_object)
    user_interface.menu()


if __name__ == "__main__":
    main()
