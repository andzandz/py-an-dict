import unittest
from AnDict import AnDict


class AnDictTest(unittest.TestCase):
    def setUp(self):
        self.ad = AnDict.AnDict()

    def testSingleEntry(self):
        self.ad.put('a', 1)
        self.assertEqual(1, self.ad.get('a'))

    def testTwoEntries(self):
        self.ad.put('a', 1)
        self.ad.put('b', 2)
        self.assertEqual(1, self.ad.get('a'))
        self.assertEqual(2, self.ad.get('b'))

    def testSize(self):
        self.assertEqual(0, self.ad.size())
        self.ad.put('a', 1)
        self.assertEqual(1, self.ad.size())
        self.ad.put('b', 2)
        self.assertEqual(2, self.ad.size())

    def testOverwriteKey(self):
        self.ad.put('a', 1)
        self.ad.put('a', 2)
        self.assertEqual(2, self.ad.get('a'))
        self.assertEqual(1, self.ad.size())

    def testNonexistentItem(self):
        with self.assertRaises(AnDict.NonexistentKeyError):
            self.ad.get('foo')

        self.ad.put('foo', 'bar')
        self.ad.get('foo')


if __name__ == '__main__':
    unittest.main()
