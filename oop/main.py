if __name__ == "__main__":
    # Création des objets
    book = Book("Pride and Prejudice", "Jane Austen")
    ebook = EBook("Snow Crash", "Neal Stephenson", 500)
    print_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    
    # Test de la bibliothèque
    lib = Library()
    lib.add_book(book)
    lib.add_book(ebook)
    lib.add_book(print_book)
    lib.list_books()
