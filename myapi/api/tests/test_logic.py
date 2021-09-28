from django.test import TestCase

from api.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(10, 5, '+')
        self.assertEqual(15 , result)

    def test_minus(self):
        result = operations(4, 1, "-")
        self.assertEqual(3, result)

    def test_multiply(self):
        result = operations(6, 3, "*")
        self.assertEqual(18, result)

