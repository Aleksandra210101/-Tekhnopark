"""
Test for equation.py
"""
import unittest
import equation


class NamesTest(unittest.TestCase):
    """Test for 'equation.py'."""
    def test_solve_linear(self):
        """Test for solve_linear"""
        self.assertEqual(equation.solve_linear(1, 2), -2)
        self.assertEqual(equation.solve_linear(0, 2), None)
        self.assertEqual(equation.solve_linear(3, 0), 0)
        self.assertEqual(equation.solve_linear(0, 0), None)

    def test_solve_quadratic(self):
        """Test for solve_quadratic"""
        self.assertEqual(equation.solve_quadratic(2, 4, 2), -1)
        self.assertEqual(equation.solve_quadratic(5, 6, 1), (-0.2, -1.0))

    def test_num_get_root(self):
        """Test for num_get_root"""
        self.assertEqual(equation.num_get_roots(5, 6, 1), 2)
        self.assertEqual(equation.num_get_roots(0, 1, 2), 1)
        self.assertEqual(equation.num_get_roots(0, 0, 2), 0)


unittest.main()
