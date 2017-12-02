
# use_case = SumCalculateUseCase(repository)
# request = SumCalculateRequest(X=10, Y=20)
from calculator.step_3_use_case.calculation_repository import CalculationRepository
from calculator.step_3_use_case.sum_calculation import SumCalculation, SumCalculationInput, Calculation


class SumCalculateRequest:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y


class SumCalculateResponse:

    def __init__(self, calculation_id):
        self.calculation_id = calculation_id


class SumCalculateUseCase:

    def __init__(self, repository: CalculationRepository):
        self.repository = repository

    def execute(self, request: SumCalculateRequest):
        X = request.X
        Y = request.Y

        input_data = SumCalculationInput(X, Y)
        calc_result = SumCalculation().calculate(input_data)

        calculation = Calculation(input_data, calc_result)
        calculation_id = self.repository.append_calculation(calculation)
        result = SumCalculateResponse(calculation_id)

        return result
