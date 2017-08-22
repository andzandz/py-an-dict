import unittest
from AnDict import AnDict


class AnDictTest(unittest.TestCase):
    def testSingleEntry(self):
        ad = AnDict.AnDict()
        ad.put('a', 1)
        self.assertEqual(1, ad.get('a'))

    def testTwoEntries(self):
        ad = AnDict.AnDict()
        ad.put('a', 1)
        ad.put('b', 2)
        self.assertEqual(1, ad.get('a'))
        self.assertEqual(2, ad.get('b'))

    def testSize(self):
        ad = AnDict.AnDict()
        self.assertEqual(0, ad.size())
        ad.put('a', 1)
        self.assertEqual(1, ad.size())
        ad.put('b', 2)
        self.assertEqual(2, ad.size())

if __name__ == '__main__':
    unittest.main()
