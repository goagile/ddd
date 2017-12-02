from calculator.step_2_sum_calculation_persist.sum_calculation import Calculation


class NotFoundCalculation(Exception):
    pass


class CalculationRepository:

    def __init__(self):
        self.calculations = {}
        self.ids = iter([1, 2, 3])

    def _next_id(self):
        return next(self.ids)

    def append_calculation(self, calculation: Calculation):
        calculation_id = self._next_id()
        self.calculations[calculation_id] = calculation.dumps()
        return calculation_id

    def find_calculation_by_id(self, calculation_id) -> Calculation:
        calculation = self.calculations.get(calculation_id)
        if not calculation:
            raise NotFoundCalculation
        result = Calculation.load(calculation)
        return result
