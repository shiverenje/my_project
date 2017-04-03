import unittest
from boot import culate


class Tester_code(unittest.TestCase):
    def test_months(self):
       # self.assertRaises(ValueError, culate, 100, 36, 1)
        self.assertRaises(culate(12000,25,1),ValueError)

