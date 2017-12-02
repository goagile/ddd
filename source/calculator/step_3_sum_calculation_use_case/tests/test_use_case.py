import unittest

from calculator.step_2_sum_calculation_persist.sum_calculation import (
    SumCalculationInput,
    SumCalculationResult
)
from calculator.step_3_sum_calculation_use_case.calculation_repository import CalculationRepository
from calculator.step_3_sum_calculation_use_case.sum_calculation import Calculation
from calculator.step_3_sum_calculation_use_case.use_case import SumCalculateUseCase, SumCalculateRequest


class TestSumCalculateUseCase(unittest.TestCase):

    def test__sum_calculate_use_case__return_calculation_id(self):
        """
            тестируется вычисление суммы двух чисел
            выполняется вариант использования
            репозиторий должен вернуть идентификатор сохраненной записи
        """
        expected = 1
        repository = CalculationRepository()
        use_case = SumCalculateUseCase(repository)
        request = SumCalculateRequest(X=10, Y=20)
        response = use_case.execute(request)

        result = response.calculation_id

        self.assertEqual(expected, result)

    def test__repository__save_calculation(self):
        """
            тестируется вычисление суммы двух чисел
            выполняется вариант использования
            в репозиторий должен сохраниться верный результат
        """
        expected = Calculation(
            input_data=SumCalculationInput(X=10, Y=20),
            calc_result=SumCalculationResult(Z=30)
        )
        repository = CalculationRepository()
        use_case = SumCalculateUseCase(repository)
        request = SumCalculateRequest(X=10, Y=20)
        response = use_case.execute(request)
        calculation_id = response.calculation_id

        result = repository.find_calculation_by_id(calculation_id)

        self.assertEqual(expected, result)
