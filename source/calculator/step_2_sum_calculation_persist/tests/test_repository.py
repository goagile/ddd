import unittest

from calculator.step_2_sum_calculation_persist.calculation_repository import (
    CalculationsRepository,
    NotFoundCalculation
)
from calculator.step_2_sum_calculation_persist.sum_calculation import (
    Calculation,
    SumCalculationInput,
    SumCalculationResult
)


class TestCalculationsRepository(unittest.TestCase):

    def test__append_calculation(self):
        expected = 1
        calculation = Calculation(
            input_data=SumCalculationInput(X=10, Y=20),
            calc_result=SumCalculationResult(Z=30)
        )
        repository = CalculationsRepository()

        result = repository.append_calculation(calculation)

        self.assertEqual(expected, result)

    def test__not_found_calculation(self):
        repository = CalculationsRepository()

        with self.assertRaises(NotFoundCalculation):
            repository.find_calculation_by_id(1)
