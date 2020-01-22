import re
import book
import customer
import bookstore_database
import os



class UserInterface:
    def __init__(self):
        pass

        # def __init__(self, database_object): # było
        #     self.database_object = database_object

    def menu(self):
        quit_program = False
        while not quit_program:
            print("\nChoose number from menu:")
            print("1. Add new customer")
            print("2. Add new book")
            print("3. Show all customers")
            print("4. Show all books")
            print("5. --------- Order the book on the customer's account")
            print("6. --------- Delete customer")
            print("7. Delete book")
            print("0. Quit bookstore")
            is_number_error = True
            while is_number_error:
                try:
                    chosen_number = input("Pass number (0 - 4): ")
                    chosen_number_int = int(chosen_number)
                    if chosen_number_int not in range(0, 8):  # or [0, 1, 2, 3, 4, 5, 6, 7]
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
            if chosen_number_int == 5:
                self.order_book()
            if chosen_number_int == 6:
                self.delete_customer()
            if chosen_number_int == 7:
                self.delete_book()
            if chosen_number_int == 0:
                print("Bye bye")
                quit_program = True

    # selects customer's pesel
    def select_customer_pesel(self):
        self.all_customers()

        is_pesel_error = True
        while is_pesel_error:
            try:
                passed_pesel = input("\nPass customer's pesel: ")
                int(passed_pesel)  # check if pesel contains only numbers
                if len(passed_pesel) != 11:
                    raise Exception()
                is_pesel_error = False
            except ValueError as e:
                print(passed_pesel + " does not consist of integers")
            except Exception as e:
                print("Pesel should consist of 11 digits")

        # for c in self.database_object.customers:
        #     c = str(c)
        #     if c.find(passed_pesel): # if c contains passed_pesel
        #         print("You have selected customer:")
        #         # c.toString()
        #         print(c)
        #         return c
        # selected_customer = c # chyba nie dziala
        # return selected_customer # chyba nie dziala

        with open("file_customers.txt") as file_customers_object:  # opens existing file
            for row in file_customers_object:
                if row.find(passed_pesel) != -1:  # if row contains passed_pesel then find() returns index of first letter of passed_pesel. If doesn't contain then returns -1
                    print("You have selected customer:")
                    print(row)
                    # print(type(row))
                    return passed_pesel

    # selects book's number
    def select_book_number(self):

        print("\nALL BOOKS NUMBERED:")
        # loop from 0 to len(self.database_object.books) - 1
        # for i in range(len(self.database_object.books)):
        #     print(str(i+1))
        #     self.database_object.books[i].toString()  # 1 None

        # for i, book in enumerate(self.database_object.books):
        #     print(str(i + 1))
        #     book.toString()

        # file_books_object = open("file_books.txt")
        # file_books_object_length = len(file_books_object)

        ##########################################################

        before_enumerate_list = list()

        with open("file_books.txt") as file_books_object:  # opens existing file
            for row in file_books_object:
                before_enumerate_list.append(row)

        for element in before_enumerate_list:
            if element == "\n":
                before_enumerate_list.remove(element)

        with open("file_books.txt", "w") as file_books_object:  # opens existing file
            for row in range(0, len(before_enumerate_list)):
                file_books_object.write(before_enumerate_list[row] + "\n")

        ##########################################################

        file_books_object_amount_of_rows = 0

        # shows all rows with numbers
        with open("file_books.txt") as file_books_object:  # opens existing file
            for i, row in enumerate(file_books_object):
                if row != "\n":
                    print(str(round((i + 2)/2)) + ". " + row)
                    # print(type(row))
                    file_books_object_amount_of_rows = file_books_object_amount_of_rows + 1  # counts amount of rows

        is_book_error = True
        while is_book_error:
            try:
                chosen_number = input("Pass book number: ")
                chosen_number_int = int(chosen_number)
                if chosen_number_int < 1 or chosen_number_int > file_books_object_amount_of_rows:  # was chosen_number_int > len(self.database_object.books)
                    raise NameError()
                is_book_error = False
            except ValueError as e:
                print(chosen_number + " is not an integer")
            except NameError as e:
                print(chosen_number + " is out of the list of books")

        # selected_book = self.database_object.books[chosen_number_int - 1] # było
        # return selected_book

        # selects row which has number chosen_number_int
        with open("file_books.txt") as file_books_object:  # opens existing file
            for i, row in enumerate(file_books_object):
                # print(str(i + 1) + ". " + row)
                if i == chosen_number_int - 1:
                    print("You have selected book:")
                    print(row)  # shows whole book but method returns only her number
                    return chosen_number

    # assins selected customer's pesel to selected book number
    def assign_selected_customer_pesel_to_selected_book(self, selected_customer_pesel, selected_book_number):
        with open("file_books.txt", "a") as file_books_object:  # opens existing file
            for i, row in enumerate(file_books_object):
                # print(str(i + 1) + ". " + row)
                if i == int(selected_book_number) - 1:
                    re.sub("None", selected_customer_pesel, row)  # sub() substitutes "None" to selected_customer_pesel in text from row

    # 1
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

        is_pesel_error = True
        while is_pesel_error:
            try:
                passed_pesel = input("Pass new customer's pesel: ")
                int(passed_pesel)  # check if pesel contains only numbers
                if len(passed_pesel) != 11:
                    raise Exception()
                is_pesel_error = False
            except ValueError as e:
                print(passed_pesel + " does not consist of integers")
            except Exception as e:
                print("Pesel should consist of 11 digits")

        new_customer.pesel = passed_pesel
        print("You have added a new customer: ")
        # customer_as_string = new_customer.toString() # zrezygnowałem
        new_customer.toString()
        # print(str(new_customer.first_name) + " " + str(new_customer.last_name) + " " + str(new_customer.pesel))

        # saves new customer to database_object.customers
        # self.database_object.customers.add(new_customer) # was
        print("po wyświetleniu toString()")
        # self.database_object.customers.add(new_customer.toString())
        # self.database_object.customers.add(customer_as_string) # zrezygnowalem z database

        # saves new customer to file_customers.txt
        with open("file_customers.txt", "a") as file_customers_object:  # opens existing file
            file_customers_object.write(
                new_customer.first_name + " " + new_customer.last_name + " " + new_customer.pesel + "\n")
            # file_customers_object.write(str(customer_as_string) + "\n")

    # 2
    def add_book(self):
        new_book = book.Book()
        passed_title = input("Pass new book's title: ")
        new_book.title = passed_title
        passed_author_name = input("Pass new book's author's name: ")
        new_book.author_name = passed_author_name
        passed_author_surname = input("Pass new book's author's surname: ")
        new_book.author_surname = passed_author_surname

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
        # new_book.toString()
        # book_as_string = new_book.toString() # zrezygnowałem
        new_book.toString()

        # saves new customer to database_object.books
        # self.database_object.books.append(new_book)
        # self.database_object.books.append(new_book.toString())
        # self.database_object.books.append(book_as_string) # zrezygnowałem

        # saves new book to file_books.txt
        with open("file_books.txt", "a") as file_books_object:  # opens existing file
            file_books_object.write(
                new_book.title + " " + new_book.author_name + " " + new_book.author_surname + " " + str(
                    new_book.price) + " " + str(new_book.buyer_pesel) + "\n")
            # file_customers_object.write(str(customer_as_string) + "\n")

    # 3
    def all_customers(self):
        print("\nCustomers details from file_customers.txt:\n")
        with open("file_customers.txt") as file_customers_object:  # opens existing file
            for row in file_customers_object:
                if row != "\n":  # prints only not empty lines
                    print(row)
                # self.database_object.customers.add(row)
        # for c in self.database_object.customers:
        #     c.toString()

    # 4
    def all_books(self):
        print("\nBooks details from file_books.txt:\n")
        with open("file_books.txt") as file_books_object:  # opens existing file
            for row in file_books_object:
                if row != "\n":  # prints only not empty lines
                    print(row)
        # for b in self.database_object.books:
        #     b.toString()

    # 5
    def order_book(self):
        selected_customer_pesel = self.select_customer_pesel()
        print("Pesel of selected customer: " + selected_customer_pesel)
        selected_book_number = self.select_book_number()
        print("Number of selected book: " + selected_book_number)
        self.assign_selected_customer_pesel_to_selected_book(selected_customer_pesel, selected_book_number)
        # selected_book.buyer_pesel = selected_customer.pesel # było

    # 7
    def delete_book(self):
        selected_book_number = self.select_book_number()
        before_delete_list = list()

        with open("file_books.txt") as file_books_object:  # opens existing file
            for row in file_books_object:
                before_delete_list.append(row)

        for element in before_delete_list:
            if element == "\n":
                before_delete_list.remove(element)

        print("List of books before delete: ", before_delete_list)
        print("Length of that list: ", len(before_delete_list))
        try:
            before_delete_list.pop(int(selected_book_number) - 1)  # deletes row from before_delete_list
        except ValueError:
            print("Out of list. Pass again number of book which you want to delete")
            self.delete_book()

        for element in before_delete_list:
            if element == "\n":
                before_delete_list.remove(element)

        after_delete_list = before_delete_list
        print("List of books after delete: ", after_delete_list)
        after_delete_list_length = len(after_delete_list)
        print("Length of that list: ", after_delete_list_length)

        # os.remove("file_books.txt")
        # file_books_object = open("file_books.txt", "w")  # creates file_customers.txt
        # file_books_object.close()
        #
        with open("file_books.txt", "w") as file_books_object:  # opens existing file
            for row in range(0, after_delete_list_length):
                file_books_object.write(after_delete_list[row] + "\n")


def main():
    # opens and closes files or creates new txt files if there are not
    try:
        with open("file_customers.txt") as file_customers_object:  # tries to open file (if it exists)
            print("\nCustomers loaded.")
    except FileNotFoundError:
        print("Creates new file_customers.txt")
        file_customers_object = open("file_customers.txt", "w")  # creates file_customers.txt if it does not exists
        file_customers_object.close()
    print("Is file_customers.txt closed?: " + str(file_customers_object.closed))

    try:
        with open("file_books.txt") as file_books_object:  # tries to open file (if it exists)
            print("\nBooks loaded.")
    except FileNotFoundError:
        print("Creates new file_books.txt")
        file_books_object = open("file_books.txt", "w")  # creates file_customers.txt if it does not exists
        file_books_object.close()
    print("Is file_books.txt closed?: " + str(file_books_object.closed))

    # database_object = bookstore_database.BookstoreDatabase() # było
    # user_interface = UserInterface(database_object) # było
    user_interface = UserInterface()
    user_interface.menu()


if __name__ == "__main__":
    main()
