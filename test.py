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

    def test_can_calculate_when_only_capacity_is_deal_with(self):
        """
        Объем прокатки = 20 тонн/час
        Грузоподъемность 1 грузовика = 5 тонн -> 4 разгрузки
        Время разгрузки = 30 мин
        """
        expected = 2
        tc = TruckCalculation()
        tc.milling_capacity = 20
        tc.truck_capacity = 5
        tc.unloading_time = 30

        result = tc.need_number_of_trucks

        self.assertEqual(expected, result)


class TruckCalculation:

    def __init__(self):
        self.milling_capacity = 0
        self.truck_capacity = 0
        self.unloading_time = 0

    @property
    def need_number_of_trucks(self):
        if self._is_not_calculatable():
            return 0
        number_of_unloadings = 60 / self.unloading_time
        shuttle_capacity = self.truck_capacity * number_of_unloadings
        return self.milling_capacity / shuttle_capacity

    def _is_not_calculatable(self):
        return bool(self.truck_capacity == 0 or self.unloading_time == 0)
