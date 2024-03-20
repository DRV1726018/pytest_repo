import unittest
from calculadora import suma, resta

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), "error")
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)
        self.assertEqual(resta(10, 5), 5)
        self.assertEqual(resta(100, 100), 0)

if __name__ == '__main__':
    unittest.main()