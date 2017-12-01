import unittest

from calculator.sum_calculation import SumCalculationResult, SumCalculationInput, Calculation, SumCalculation


class TestSumCalculation(unittest.TestCase):

    def test__calculate_10_20__returns_30(self):
        expected = SumCalculationResult(Z=30)
        input_data = SumCalculationInput(X=10, Y=20)
        sum_calc = SumCalculation()

        result = sum_calc.calculate(input_data)

        self.assertEqual(expected, result)


class TestSumCalculationResult(unittest.TestCase):

    def test_dumps(self):
        expected = dict(Z=30)
        scr = SumCalculationResult(Z=30)

        result = scr.dumps()

        self.assertEqual(expected, result)

    def test_loads(self):
        expected = SumCalculationResult(Z=30)
        dumped = dict(Z=30)

        result = SumCalculationResult.load(dumped)

        self.assertEqual(expected, result)


class TestCalculation(unittest.TestCase):

    def test_dumps(self):
        expected = dict(
            input_data=dict(X=10, Y=20),
            calc_result=dict(Z=30)
        )
        calc_result = SumCalculationResult(Z=30)
        input_data = SumCalculationInput(X=10, Y=20)
        c = Calculation(input_data, calc_result)

        result = c.dumps()

        self.assertEqual(expected, result)

    def test_loads(self):
        expected = Calculation(
            input_data=SumCalculationInput(X=10, Y=20),
            calc_result=SumCalculationResult(Z=30)
        )
        dumped = dict(
            input_data=dict(X=10, Y=20),
            calc_result=dict(Z=30)
        )
        result = Calculation.load(dumped)

        self.assertEqual(expected, result)
