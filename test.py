import unittest


class Test(unittest.TestCase):

    def test_will_get_zero_as_result__when_no_input_is_given(self):
        expected = 0
        tc = TruckCalculation()
        result = tc.need_number_of_trucks

        self.assertEqual(expected, result)

    @unittest.skip('Округление десятичных значений количества грузовиков')
    def test_cannot_round_decimal_truck_down(self):
        pass


class TruckCalculation:

    def __init__(self):
        self.need_number_of_trucks = -1
