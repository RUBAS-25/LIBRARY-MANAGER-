# library_manager.py

import os
import json

# Load library from a file
def load_library(filename="library.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Save library to a file
def save_library(library, filename="library.txt"):
    with open(filename, "w") as file:
        json.dump(library, file, indent=4)

# Add a new book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: ").strip())
    except ValueError:
        print("Invalid year. Book not added.")
        return
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = read_input == 'yes'

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    library.append(book)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    if choice not in ["1", "2"]:
        print("Invalid choice.")
        return
    
    keyword = input("Enter the title/author to search: ").strip().lower()
    matches = []
    
    for book in library:
        if (choice == "1" and keyword in book["title"].lower()) or \
           (choice == "2" and keyword in book["author"].lower()):
            matches.append(book)

    if matches:
        print("\nMatching Books:")
        for idx, book in enumerate(matches, start=1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Library is empty.")
        return
    print("\nYour Library:")
    for idx, book in enumerate(library, start=1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Display statistics
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("No books in library.")
        return
    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage_read:.1f}%")

# Main menu
def menu():
    library = load_library()

    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
