class Library:
    def __init__(self, book_name, author, availability_status=True):
        self.book_name = book_name
        self.author = author
        self.availability_status = availability_status

    def checkout_book(self):
        if self.availability_status:
            self.availability_status = False
            print(self.book_name,' has been checked out.')
        else:
            print(self.book_name,' is currently not available.')

    def return_book(self):
        if not self.availability_status:
            self.availability_status = True
            print(self.book_name,'has been returned.')
        else:
            print(self.book_name,' was not checked out.')

    def display_available_books(books):
        print("\nAvailable Books:")
        available = False
        for book in books:
            if book.availability_status:
                print(f'- {book.book_name} by {book.author}')
                available = True
        if not available:
            print("No books are currently available.")


book1 = Library("Python Basics", "John Smith")
book2 = Library("Data Science 101", "Alice Brown")
book3 = Library("Machine Learning", "David Lee")

books_list = [book1, book2, book3]

Library.display_available_books(books_list)

book1.checkout_book()
Library.display_available_books(books_list)

book1.return_book()
Library.display_available_books(books_list)
