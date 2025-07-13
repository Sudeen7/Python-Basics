"""
library management:
takes options for add books, get total number of books and get list of available books as input
"""
class Library:
    def __init__(self):
        '''
        no_of_books = int
        books = list
        '''
        self.no_of_books = 0
        self.books = []  # list

    def addBook(self):
        self.bookName = input("Enter the name of book to add: ")
        self.books.append(self.bookName)  # append input book to the list
        self.no_of_books += 1  # increment the number of books by 1

    def printBooks(self):
        if self.books:  # check if the list contains at least one book
            sort_books = sorted(self.books)  # new sorted list
            print("Books available in the library are: ")
            for book in sort_books:
                print(book)
        else:
            print("No books in the library.")

    def get_no_of_books(self):
        return self.no_of_books


def main():
    obj = Library()
    print("-----Welcome to the Library!-----")
    while True:
        user = input(
            "Enter '1' to add books, '2' to get the number of books and '3' to get the list of available books, or 'q' to quit: ")
        if user == "1":
            obj.addBook()
        elif user == "2":
            print(
                f"Number of books in the library are: {obj.get_no_of_books()}")
        elif user == "3":
            print(f"Available books in the library: {obj.printBooks()}")
        elif user.lower() == "q":
            print("Thank you!")
            break
        else:
            print("Invalid Request!")
            break


main()
