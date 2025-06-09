import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test suite for SimpleCalculator class operations"""
    
    def setUp(self):
        """Create a calculator instance before each test"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test addition with various numeric combinations"""
        # Nombres positifs
        self.assertEqual(self.calc.add(5, 3), 8)
        # Nombres négatifs
        self.assertEqual(self.calc.add(-4, -2), -6)
        # Mix positif/négatif
        self.assertEqual(self.calc.add(10, -5), 5)
        # Zéros
        self.assertEqual(self.calc.add(0, 0), 0)
        # Décimaux
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6, places=2)
    
    def test_subtraction(self):
        """Test subtraction with various numeric combinations"""
        # Nombres positifs
        self.assertEqual(self.calc.subtract(10, 4), 6)
        # Nombres négatifs
        self.assertEqual(self.calc.subtract(-3, -1), -2)
        # Mix positif/négatif
        self.assertEqual(self.calc.subtract(5, -2), 7)
        # Zéros
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Décimaux
        self.assertAlmostEqual(self.calc.subtract(7.5, 2.5), 5.0, places=2)
    
    def test_multiplication(self):
        """Test multiplication with various numeric combinations"""
        # Nombres positifs
        self.assertEqual(self.calc.multiply(6, 7), 42)
        # Nombres négatifs
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        # Mix positif/négatif
        self.assertEqual(self.calc.multiply(5, -3), -15)
        # Multiplication par zéro
        self.assertEqual(self.calc.multiply(0, 100), 0)
        # Décimaux
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0, places=2)
    
    def test_division(self):
        """Test division with various numeric combinations and edge cases"""
        # Division normale
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Division négative
        self.assertEqual(self.calc.divide(-15, 3), -5)
        # Division décimale
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5, places=2)
        # Division par un nombre négatif
        self.assertEqual(self.calc.divide(20, -5), -4)
        # Division de zéro
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Division par zéro (cas limite)
        self.assertIsNone(self.calc.divide(10, 0))
        # Division de zéro par zéro
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    unittest.main()
