def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers do not have factorials.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
    
import unittest

class TestFactorialFunction(unittest.TestCase):
    def test_factorial(self):
        # Normal cases
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_negative_input(self):
        # Check if ValueError is raised for negative input
        with self.assertRaises(ValueError):
            factorial(-3)

# This runs the test when the file is executed directly
if __name__ == '__main__':
    unittest.main()
