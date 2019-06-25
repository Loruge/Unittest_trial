import unittest
from my_code import *


class TestLionCode(unittest.TestCase):

    def test_animal_lion_tail(self):
        self.assertEqual(lion.tail, 1, 'wrong')

    def test_animal_lion_paw(self):
        self.assertEqual(lion.paw, 4, 'wrong')

    def test_animal_lion_wool(self):
        self.assertTrue(lion.wool, True)

    def test_animal_lion_tail_0(self):
        self.assertEqual(lion.tail, 0, 'wrong')

    def test_animal_lion_tail_2(self):
        self.assertEqual(lion.tail, 2, 'wrong')

    def test_animal_lion_paw_3(self):
        self.assertEqual(lion.paw, 3, 'wrong')

    def test_animal_lion_paw_5(self):
        self.assertEqual(lion.paw, 5, 'wrong')

    def test_animal_lion_wool_f(self):
        self.assertFalse(lion.wool, True)
