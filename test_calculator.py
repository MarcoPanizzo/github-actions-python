# test_calculator.py
import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # 2 + 3 should equal 5
        self.assertEqual(add(-1, 1), 0)  # -1 + 1 should equal 0
        self.assertEqual(add(0, 0), 0)    # 0 + 0 should equal 0

if __name__ == "__main__":
    unittest.main()
