class Book:
    """Représente un livre dans la bibliothèque avec son état d'emprunt"""
    
    def __init__(self, title: str, author: str):
        """
        Initialise un nouveau livre
        
        Args:
            title: Titre du livre
            author: Auteur du livre
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Disponible par défaut

    def check_out(self):
        """Marque le livre comme emprunté"""
        self._is_checked_out = True

    def return_book(self):
        """Marque le livre comme retourné (disponible)"""
        self._is_checked_out = False

    def is_available(self) -> bool:
        """Vérifie si le livre est disponible à l'emprunt"""
        return not self._is_checked_out

    def __str__(self):
        """Représentation textuelle du livre"""
        return f"{self.title} by {self.author}"


class Library:
    """Gère une collection de livres et les opérations d'emprunt"""
    
    def __init__(self):
        """Initialise une bibliothèque avec une collection vide de livres"""
        self._books = []

    def add_book(self, book: Book):
        """
        Ajoute un livre à la bibliothèque
        
        Args:
            book: Instance de Book à ajouter
        """
        self._books.append(book)

    def check_out_book(self, title: str):
        """
        Emprunte un livre par son titre
        
        Args:
            title: Titre du livre à emprunter
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return

    def return_book(self, title: str):
        """
        Retourne un livre emprunté par son titre
        
        Args:
            title: Titre du livre à retourner
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return

    def list_available_books(self):
        """Liste tous les livres disponibles dans la bibliothèque"""
        for book in self._books:
            if book.is_available():
                print(book)
