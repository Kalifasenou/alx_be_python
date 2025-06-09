class BankAccount:
    """
    Représente un compte bancaire avec des opérations de base
    
    Attributes:
        account_balance (float): Solde actuel du compte
    """
    
    def __init__(self, initial_balance=0.0):
        """
        Initialise un nouveau compte bancaire
        
        Args:
            initial_balance (float, optional): Solde initial. Par défaut 0.0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Effectue un dépôt sur le compte
        
        Args:
            amount (float): Montant à déposer
        """
        if amount > 0:
            self.account_balance += amount
        else:
            raise ValueError("Le montant doit être positif")

    def withdraw(self, amount):
        """
        Effectue un retrait si les fonds sont suffisants
        
        Args:
            amount (float): Montant à retirer
            
        Returns:
            bool: True si retrait réussi, False sinon
        """
        if amount <= self.account_balance and amount > 0:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Affiche le solde actuel formaté"""
        print(f"Current Balance: ${self.account_balance:.2f}")
