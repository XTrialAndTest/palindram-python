import unittest
from currency import currency
print(currency(19899,134.5))

class CurrencyTrest(unittest.TestCase):
    def test_currency(self):
        a=19899
        b=134.5
        self.assertEqual(currency(19899, 134.5),a/b )

if __name__=='__main__':
    unittest.main()
