import unittest
from  hw_oop import *

class TestShape(unittest.TestCase):
    def setUp(self):
        self.rectangle = Ractangle(3,4)
        self.circle = Circla(15)
        self.triangle = Triangle(5,6,3)

    def test_color_rectangle(self):
        rec = self.rectangle.color()
        self.assertEqual(rec,'Black')

    def test_add_rectangle(self):
        rec = self.rectangle.__add__(self.triangle)
        self.assertEqual(rec,27)

    def test_sub_rectangle(self):
        rec = self.rectangle.__sub__(self.triangle)
        self.assertEqual(rec, -3)

    def test_eq_rectangle(self):
        rec = self.rectangle.__eq__(self.triangle)
        self.assertEqual(rec, False)
        



unittest.main()