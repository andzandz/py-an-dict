import unittest
from AnDict import AnDict


class AnDictTest(unittest.TestCase):
    def test_upper(self):
        ad = AnDict.AnDict()
        ad.put('a', 1)
        self.assertEqual(ad.get('a'), 1)

if __name__ == '__main__':
    unittest.main()
