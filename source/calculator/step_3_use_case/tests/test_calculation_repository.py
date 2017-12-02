import unittest

from calculator.step_3_use_case.calculation_repository import (
    CalculationRepository,
    NotFoundCalculation
)
from calculator.step_3_use_case.sum_calculation import (
    Calculation,
    SumCalculationInput,
    SumCalculationResult
)


calculation = Calculation(
    input_data=SumCalculationInput(X=10, Y=20),
    calc_result=SumCalculationResult(Z=30)
)


class TestCalculationRepository(unittest.TestCase):

    def test__append_calculation(self):
        expected = 1
        repository = CalculationRepository()

        result = repository.append_calculation(calculation)

        self.assertEqual(expected, result)

    def test__find_calculation_by_id__with_not_found_calculation(self):
        repository = CalculationRepository()

        with self.assertRaises(NotFoundCalculation):
            repository.find_calculation_by_id(1)

    def test__find_calculation_by_id__with_existing_calculation(self):
        repository = CalculationRepository()
        id_ = repository.append_calculation(calculation)

        result = repository.find_calculation_by_id(id_)

        self.assertEqual(calculation, result)
