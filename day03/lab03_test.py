import unittest
from lab03 import *

class labTests(unittest.TestCase):

  def test_shout(self):
    self.assertEqual("TEST",shout("test"))
  def test_reverse(self):
    self.assertEqual("tset",reverse("test"))
    with self.assertRaises(TypeError): reverse(67)
  def test_reversewords(self):
    self.assertEqual("Lucas Is Name My Hello ",reversewords("Hello My Name Is Lucas"))
    with self.assertRaises(TypeError): reversewords([3,5,6,"Hello"])
  def test_reversewordletters(self):
    self.assertEqual("olleH yM emaN sI sacuL ",reversewordletters("Hello My Name Is Lucas"))
    with self.assertRaises(TypeError): reversewordletters([3,5,6,"Hello"])
  def test_piglatin(self):
    self.assertEqual('isThay isay aay esttay ',piglatin("This is a test"))
    with self.assertRaises(TypeError): reverse(54234)

if __name__ == '__main__':
  unittest.main()
