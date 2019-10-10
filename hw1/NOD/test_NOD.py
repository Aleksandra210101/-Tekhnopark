"""
Test for NOD.py
"""
import unittest
from NOD import nod

class NamesTestCase(unittest.TestCase):
    """Тесты для 'NOD.py'."""
    def test_nod(self):
        self.assertEqual(nod(30, 5), 5)
        self.assertEqual(nod(1200, 200), 200)

unittest.main()








