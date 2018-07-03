import unittest
from hashmap import Hashmap

class TestHashmapMethods(unittest.TestCase):

    def setUp(self):
        self.hashmap = Hashmap()

    def test_putGet(self):
        self.hashmap.put("foo", "bar")
        self.assertEqual(self.hashmap.elements, 1)
        self.assertEqual(self.hashmap.get("foo"), "bar")

    def test_overwritesSameKey(self):
        self.hashmap.put("foo", "bar")
        self.hashmap.put("foo", "newbar")
        self.assertEqual(self.hashmap.elements, 1)
        self.assertEqual(self.hashmap.get("foo"), "newbar")

    def test_solvesCollision(self):
        self.hashmap.put("abab", "newbar")
        self.hashmap.put("baba", "boobar")
        self.assertEqual(self.hashmap.elements, 2)
        self.assertEqual(self.hashmap.get("baba"), "boobar")
        self.assertEqual(self.hashmap.get("abab"), "newbar")

    def test_resizesAndCopies(self):
        self.hashmap.put("foo", "newbar")
        self.hashmap.put("boo", "boobar")
        self.hashmap.put("fooo", "newbaro")
        self.hashmap.put("booo", "boobaro")
        self.hashmap.put("foooo", "newbaroo")
        self.hashmap.put("boooo", "boobaroo")
        self.hashmap.put("fooooo", "newbarooo")
        self.assertEqual(self.hashmap.elements, 7)
        self.assertEqual(self.hashmap.size, 10)
        self.hashmap.put("booooo", "boobarooo")
        self.assertEqual(self.hashmap.elements, 8)
        self.assertEqual(self.hashmap.size, 20)
        self.assertEqual(self.hashmap.get("boooo"), "boobaroo")

if __name__ == '__main__':
    unittest.main()
