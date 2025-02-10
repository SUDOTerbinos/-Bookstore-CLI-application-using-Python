import json

BOOKS_FILE = "books.json"

def load_books():
    """Load books from a JSON file."""
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    """Save books to a JSON file."""
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    """Add a new book to the store."""
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    price = input("Enter book price: ")
    
    books = load_books()
    books.append({"title": title, "author": author, "price": price})
    save_books(books)
    print(f"Book '{title}' added successfully!\n")

def view_books():
    """Display all books."""
    books = load_books()
    if not books:
        print("No books available.\n")
    else:
        print("Available Books:")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book['title']} by {book['author']} - ${book['price']}")
        print()

def search_book():
    """Search for a book by title."""
    search_title = input("Enter book title to search: ").lower()
    books = load_books()
    
    found_books = [book for book in books if search_title in book['title'].lower()]
    
    if found_books:
        print("Search Results:")
        for book in found_books:
            print(f"{book['title']} by {book['author']} - ${book['price']}")
    else:
        print("No book found with that title.")
    print()

def delete_book():
    """Delete a book by title."""
    delete_title = input("Enter book title to delete: ").lower()
    books = load_books()
    
    updated_books = [book for book in books if delete_title != book['title'].lower()]
    
    if len(updated_books) < len(books):
        save_books(updated_books)
        print("Book deleted successfully.\n")
    else:
        print("Book not found.\n")

def main():
    """Main function to run the bookstore app."""
    while True:
        print("\nBookstore Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Exiting...\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
