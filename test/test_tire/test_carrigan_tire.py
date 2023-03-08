import unittest
from tire.carrigan_tire import CarriganTire


class Test(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        array_tire = [0.9, 0, 0, 0]
        tire = CarriganTire(array_tire)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        array_tire = [0.8, 0, 0, 0]
        tire = CarriganTire(array_tire)

        self.assertTrue(tire.needs_service())
