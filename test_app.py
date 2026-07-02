import unittest
from app import fahrenheit_para_celsius, celsius_para_fahrenheit

class TestConversao(unittest.TestCase):
    def test_fahrenheit_para_celsius(self):
        self.assertEqual(fahrenheit_para_celsius(32), 0)
        self.assertEqual(fahrenheit_para_celsius(212), 100)

    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)
        self.assertEqual(celsius_para_fahrenheit(100), 212)

if __name__ == '__main__':
    unittest.main()