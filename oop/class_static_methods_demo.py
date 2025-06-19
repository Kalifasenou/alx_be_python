class Calculator:
    calculation_type = "Opérations Arithmétiques"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Type de calcul : {cls.calculation_type}")
        return a * b
