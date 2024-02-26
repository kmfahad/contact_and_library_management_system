import json
import re

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def update_book_status(self, isbn, new_status):
        for book in self.books:
            if book.isbn == isbn:
                book.status = new_status
                break

    def search_books(self, keyword, search_by="title"):
        result = []
        for book in self.books:
            if search_by == "title" and keyword.lower() in book.title.lower():
                result.append(book)
            elif search_by == "author" and keyword.lower() in book.author.lower():
                result.append(book)
        return result

    def save_books_to_file(self, filename):
        with open(filename, 'w') as file:
            book_data = [{'title': book.title, 'author': book.author, 'isbn': book.isbn, 'status': book.status}
                         for book in self.books]
            json.dump(book_data, file, indent=2)

    def load_books_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                book_data = json.load(file)
                self.books = [Book(**data) for data in book_data]
        except FileNotFoundError:
            print("File not found. Starting with an empty library.")

def validate_isbn(isbn):
    return bool(re.match(r'^\d{3}-\d{10}$', isbn))

def user_interface(library):
    while True:
        print("\nLibrary Management System\n")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Search Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN (e.g., 123-1234567890): ")

            if validate_isbn(isbn):
                book = Book(title, author, isbn)
                library.add_book(book)
                print("Book added successfully.")
            else:
                print("Invalid ISBN format. Please try again.")

        elif choice == "2":
            isbn = input("Enter ISBN of the book to borrow: ")
            library.update_book_status(isbn, "borrowed")
            print("Book borrowed successfully.")

        elif choice == "3":
            isbn = input("Enter ISBN of the book to return: ")
            library.update_book_status(isbn, "available")
            print("Book returned successfully.")

        elif choice == "4":
            keyword = input("Enter search keyword: ")
            search_by = input("Search by (title/author): ").lower()
            result = library.search_books(keyword, search_by)
            if result:
                print("\nSearch Results:")
                for book in result:
                    print(f"{book.title} by {book.author} (ISBN: {book.isbn}, Status: {book.status})")
            else:
                print("No matching books found.")

        elif choice == "5":
            library.save_books_to_file("library_data.json")
            print("Library data saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library = Library()
    library.load_books_from_file("library_data.json")
    user_interface(library)
