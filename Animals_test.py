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


class TestDogCode(unittest.TestCase):

    def test_animal_dog_tail(self):
        self.assertEqual(dog.tail, 1, 'wrong')

    def test_animal_dog_paw(self):
        self.assertEqual(dog.paw, 4, 'wrong')

    def test_animal_dog_wool(self):
        self.assertTrue(dog.wool, True)

    def test_animal_dog_tail_0(self):
        self.assertEqual(dog.tail, 0, 'wrong')

    def test_animal_dog_tail_2(self):
        self.assertEqual(dog.tail, 2, 'wrong')

    def test_animal_dog_paw_3(self):
        self.assertEqual(dog.paw, 3, 'wrong')

    def test_animal_dog_paw_5(self):
        self.assertEqual(dog.paw, 5, 'wrong')

    def test_animal_dog_wool_f(self):
        self.assertFalse(dog.wool, True)


class TestCatCode(unittest.TestCase):

    def test_animal_cat_tail(self):
        self.assertEqual(cat1.tail, 1, 'wrong')

    def test_animal_cat_paw(self):
        self.assertEqual(cat1.paw, 4, 'wrong')

    def test_animal_cat_wool(self):
        self.assertTrue(cat1.wool, True)

    def test_animal_cat_tail_0(self):
        self.assertEqual(cat1.tail, 0, 'wrong')

    def test_animal_cat_tail_2(self):
        self.assertEqual(cat1.tail, 2, 'wrong')

    def test_animal_cat_paw_3(self):
        self.assertEqual(cat1.paw, 3, 'wrong')

    def test_animal_cat_paw_5(self):
        self.assertEqual(cat1.paw, 5, 'wrong')

    def test_animal_cat_wool_f(self):
        self.assertFalse(cat1.wool, True)


class TestCatSphynxCode(unittest.TestCase):

    def test_animal_sphynx_tail(self):
        self.assertEqual(cat2.tail, 1, 'wrong')

    def test_animal_sphynx_paw(self):
        self.assertEqual(cat2.paw, 4, 'wrong')

    def test_animal_sphynx_wool(self):
        self.assertFalse(cat2.wool, False)

    def test_animal_sphynx_tail_0(self):
        self.assertEqual(cat2.tail, 0, 'wrong')

    def test_animal_sphynx_tail_2(self):
        self.assertEqual(cat2.tail, 2, 'wrong')

    def test_animal_sphynx_paw_3(self):
        self.assertEqual(cat2.paw, 3, 'wrong')

    def test_animal_sphynx_paw_5(self):
        self.assertEqual(cat2.paw, 5, 'wrong')

    def test_animal_sphynx_wool_t(self):
        self.assertTrue(cat2.wool, False)


class TestRoosterCode(unittest.TestCase):

    def test_animal_rooster_tail(self):
        self.assertEqual(rooster1.tail, 1, 'wrong')

    def test_animal_rooster_paw(self):
        self.assertEqual(rooster1.paw, 2, 'wrong')

    def test_animal_rooster_wool(self):
        self.assertFalse(rooster1.wool, False)

    def test_animal_rooster_tail_0(self):
        self.assertEqual(rooster1.tail, 0, 'wrong')

    def test_animal_rooster_tail_2(self):
        self.assertEqual(rooster1.tail, 2, 'wrong')

    def test_animal_rooster_paw_1(self):
        self.assertEqual(rooster1.paw, 1, 'wrong')

    def test_animal_rooster_paw_3(self):
        self.assertEqual(rooster1.paw, 3, 'wrong')

    def test_animal_rooster_wool_t(self):
        self.assertTrue(rooster1.wool, False)
