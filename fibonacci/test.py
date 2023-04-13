import unittest
from fibonacci import fibonacci

print(fibonacci(1, 1, 10))
class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        list=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(fibonacci(1, 1, 10),list)
unittest.main()