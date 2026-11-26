class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.book_id == book.book_id:
                print("Book ID already exists!")
                return

        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if len(self.books) == 0:
            print("No books available.")
            return

        for book in self.books:
            status = "Available" if book.is_available else "Issued"
            print(
                f"ID: {book.book_id}, "
                f"Title: {book.title}, "
                f"Author: {book.author}, "
                f"Status: {status}"
            )

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def issue_book(self, book_id):
        book = self.search_book(book_id)

        if book is None:
            print("Book ID not found.")
        elif book.is_available:
            book.is_available = False
            print("Book issued successfully.")
        else:
            print("Book already issued.")

    def return_book(self, book_id):
        book = self.search_book(book_id)

        if book is None:
            print("Book ID not found.")
        elif not book.is_available:
            book.is_available = True
            print("Book returned successfully.")
        else:
            print("Book was not issued.")


def main():
    library = Library()

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book_id = int(input("Enter Book ID: "))
            book = library.search_book(book_id)

            if book:
                print("\nBook Found")
                print("ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
            else:
                print("Book ID not found.")

        elif choice == "4":
            book_id = int(input("Enter Book ID: "))
            library.issue_book(book_id)

        elif choice == "5":
            book_id = int(input("Enter Book ID: "))
            library.return_book(book_id)

        elif choice == "6":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice! Please try again.")


main()