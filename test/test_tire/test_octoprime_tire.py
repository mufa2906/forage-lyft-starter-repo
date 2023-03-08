import unittest
from tire.octoprime_tire import OctoprimeTire


class Test(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        array_tire = [0.9, 1, 1, 1]
        tire = OctoprimeTire(array_tire)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        array_tire = [0.8, 0, 0, 0]
        tire = OctoprimeTire(array_tire)

        self.assertTrue(tire.needs_service())
