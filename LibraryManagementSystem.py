# For Clear Output
import os 
os. system ("cls")
# Defining Class
class BookLibrary:
    library_books = [
    "librotrack",
    "shelfwise",
    "pagekeeper",
    "booknest",
    "stacksystem",
    "bibliotech",
    "readregistry",
    "shelflife",
    "borrowbase",
    "libraloop"
]
    borrowed_books = { }
    # User RegistrationMethod
    def user_data(self):
        self.name = input("Enter your name: ")
        while True:
            try:
                self.age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Invalid Input. Please try again with a number.")
        while True:
            try:
                self.grade = int(input("Enter your grade: "))
                break
            except ValueError:
                print("Invalid Input. Try again !")
        print(f"{self.name} of age {self.age} years and {self.grade} grade is successfully registered to Library Management System.")
    # Allowing Users to Borrow Book
    def borrow_book(self):
        self.name = input("Enter your name: ")
        self.book_name = input("Enter Book Name: ").lower()
        if self.book_name in BookLibrary.library_books :
            print("This book is available. Type borrow to borrow it.")
            user_input = input("Type Here: ").lower()
            if user_input == "borrow" :
                print(f"Book is succesfully borrowed by {self.name}.")
                BookLibrary.borrowed_books.update({self.book_name : self.name})
                BookLibrary.library_books.remove(self.book_name)
            else:
                print("Try Again with a valid response.")
        else:
            print("Book is not available yet. Try again later.")
    # Allowing Users to return borrowed book
    def return_book(self):
        self.name_of_return_book = input("Enter Book Name: ").lower()
        if self.name_of_return_book in BookLibrary.borrowed_books:
            BookLibrary.library_books.append(self.name_of_return_book)
            BookLibrary.library_books.sort()
            BookLibrary.borrowed_books.pop(self.name_of_return_book)
            print("Book is returned successfully! Thankyou <3 ")
        else:
            print("This book was not borrowed, or the book name is invalid.")
    # Allowing Librarian to Add New Books
    def add_new_book(self):
        self.new_book = input("Enter Book Name: ").lower()
        if self.new_book in BookLibrary.library_books:
            print("Book is already present.")
        else:
            BookLibrary.library_books.append(self.new_book)
            BookLibrary.library_books.sort()
            print("Book Library after adding new book: ", BookLibrary.library_books )
    # Allowing Users to look our books!
    def view_books_menu(self):
        print("Select a book for you!")
        print("Here's our book menu: ", BookLibrary.library_books)
    # Allowing Users to select what they want.
    def selection_to_do(self):
        while True:
            print("--" * 7 ,"Library Management System",  "--" * 7)
            print("Please select an option to continue: ")
            print("0. Exit")
            print("1. Register")
            print("2. View Our Book Menu")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Add New Book")
            while True:
                try:
                    self.choice = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("Please Choose Option Between 0 and 5")
            if self.choice == 1 :
                self.user_data()
            elif self.choice == 2 :
                self.view_books_menu()
            elif self.choice == 3 :
                self.borrow_book()
            elif self.choice == 0:
                print("Are you sure to exit?\n" , "(Yes/No)")
                a = input("Your choice here: ").lower()
                if a == "no":
                    continue
                else:
                    print("Exited")
                    break
            elif self.choice == 4 :
                self.return_book()
            elif self.choice == 5:
                self.add_new_book()
            else:
                print("Option not available yet.")
            while True:
                print("Press 'E' to exit and 'M' to return to options dashboard : ")
                b = input("Enter your choice: ").upper()
                if b == "E":
                    exit()
                elif b == "M":
                    break
                else:
                    print("Invalid Input! Select only 'E' or 'M'.")
user = BookLibrary()
user.selection_to_do()
