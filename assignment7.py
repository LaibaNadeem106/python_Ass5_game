from typing import List, Dict, Optional
import os

# Base class for User
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def display_user_info(self):
        print(f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}")

# Librarian class that inherits from User
class Librarian(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)

    def manage_books(self, library_manager, action: str, book: 'Book' = None):
        if action == 'add' and book:
            library_manager.add_book(book)
        elif action == 'update' and book:
            library_manager.update_book(book)
        elif action == 'delete' and book:
            library_manager.delete_book(book.book_id)
        else:
            print("Invalid action or missing book information.")

# Member class that inherits from User
class Member(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)

    def borrow_book(self, library_manager, book_id: int):
        library_manager.borrow_book(self, book_id)

    def return_book(self, library_manager, book_id: int):
        library_manager.return_book(self, book_id)

# Book class
class Book:
    def __init__(self, book_id: int, title: str, author: str, available: bool = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        availability = 'Available' if self.available else 'Unavailable'
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Availability: {availability}")

# LibraryManager class for managing users, books, and transactions
class LibraryManager:
    books_file = 'books.txt'
    users_file = 'users.txt'
    
    def __init__(self):
        self.books = self.load_books()
        self.users = self.load_users()

    # Load books from file
    def load_books(self) -> Dict[int, Book]:
        books = {}
        if os.path.exists(self.books_file):
            try:
                with open(self.books_file, 'r') as f:
                    for line in f:
                        book_data = line.strip().split(',')
                        book = Book(int(book_data[0]), book_data[1], book_data[2], book_data[3] == 'True')
                        books[book.book_id] = book
            except IOError as e:
                print(f"Error reading books file: {e}")
        return books

    # Save books to file
    def save_books(self):
        try:
            with open(self.books_file, 'w') as f:
                for book in self.books.values():
                    f.write(f"{book.book_id},{book.title},{book.author},{book.available}\n")
        except IOError as e:
            print(f"Error writing to books file: {e}")

    # Load users from file
    def load_users(self) -> Dict[int, User]:
        users = {}
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r') as f:
                    for line in f:
                        user_data = line.strip().split(',')
                        if user_data[0] == 'Librarian':
                            user = Librarian(int(user_data[1]), user_data[2], user_data[3])
                        else:
                            user = Member(int(user_data[1]), user_data[2], user_data[3])
                        users[user.user_id] = user
            except IOError as e:
                print(f"Error reading users file: {e}")
        return users

    # Save users to file
    def save_users(self):
        try:
            with open(self.users_file, 'w') as f:
                for user in self.users.values():
                    user_type = 'Librarian' if isinstance(user, Librarian) else 'Member'
                    f.write(f"{user_type},{user.user_id},{user.name},{user.email}\n")
        except IOError as e:
            print(f"Error writing to users file: {e}")

    # Add a new book
    def add_book(self, book: Book):
        if book.book_id in self.books:
            print("Book already exists.")
        else:
            self.books[book.book_id] = book
            self.save_books()
            print(f"Book '{book.title}' added.")

    # Update an existing book
    def update_book(self, book: Book):
        if book.book_id in self.books:
            self.books[book.book_id] = book
            self.save_books()
            print(f"Book '{book.title}' updated.")
        else:
            print("Book not found.")

    # Delete a book
    def delete_book(self, book_id: int):
        if book_id in self.books:
            del self.books[book_id]
            self.save_books()
            print(f"Book with ID {book_id} deleted.")
        else:
            print("Book not found.")

    # Borrow a book
    def borrow_book(self, member: Member, book_id: int):
        if book_id in self.books and self.books[book_id].available:
            self.books[book_id].available = False
            self.save_books()
            print(f"{member.name} borrowed the book '{self.books[book_id].title}'.")
        else:
            print("Book not available for borrowing.")

    # Return a book
    def return_book(self, member: Member, book_id: int):
        if book_id in self.books and not self.books[book_id].available:
            self.books[book_id].available = True
            self.save_books()
            print(f"{member.name} returned the book '{self.books[book_id].title}'.")
        else:
            print("Book was not borrowed.")

# Creating Library Manager
library_manager = LibraryManager()

# Creating a Librarian
librarian = Librarian(1, "John Doe", "johndoe@example.com")

# Adding a new book
book1 = Book(101, "The Great Gatsby", "F. Scott Fitzgerald")
librarian.manage_books(library_manager, 'add', book1)

# Updating the book information
book1_updated = Book(101, "The Great Gatsby", "F. Scott Fitzgerald", available=False)
librarian.manage_books(library_manager, 'update', book1_updated)

# Deleting a book
librarian.manage_books(library_manager, 'delete', book1)

# Creating a Member
member = Member(2, "Jane Doe", "janedoe@example.com")

# Borrowing a book
member.borrow_book(library_manager, 101)

# Returning a book
member.return_book(library_manager, 101)
