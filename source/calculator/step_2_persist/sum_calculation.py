

class SumCalculationInput:

    def __init__(self, X=10, Y=20):
        self.X = X
        self.Y = Y

    def __eq__(self, other):
        return all([
            self.X == other.X,
            self.Y == other.Y
        ])

    def dumps(self):
        result = dict(
            X=self.X,
            Y=self.Y
        )
        return result

    @classmethod
    def load(cls, dumped):
        X = dumped.get('X')
        if X is None:
            raise ValueError('X is not found')
        Y = dumped.get('Y')
        if Y is None:
            raise ValueError('Y is not found')
        result = cls(X, Y)
        return result


class SumCalculationResult:

    def __init__(self, Z=30):
        self.Z = Z

    def __eq__(self, other):
        return bool(self.Z == other.Z)

    def dumps(self):
        result = dict(
            Z=self.Z
        )
        return result

    @classmethod
    def load(cls, dumped):
        Z = dumped.get('Z')
        if Z is None:
            raise ValueError('Z is not found')
        result = cls(Z)
        return result


class Calculation:

    def __init__(self, input_data: SumCalculationInput, calc_result: SumCalculationResult):
        self.input_data = input_data
        self.calc_result = calc_result

    def __eq__(self, other):
        is_input_data_equal = bool(self.input_data == other.input_data)
        is_calc_result_equal = bool(self.calc_result == other.calc_result)
        result = is_input_data_equal and is_calc_result_equal
        return result

    def dumps(self):
        result = dict(
            input_data=self.input_data.dumps(),
            calc_result=self.calc_result.dumps()
        )
        return result

    @classmethod
    def load(cls, dumped):
        dumped_input_data = dumped.get('input_data')
        dumped_calc_result = dumped.get('calc_result')
        input_data = SumCalculationInput.load(dumped_input_data)
        calc_result = SumCalculationResult.load(dumped_calc_result)
        result = cls(input_data, calc_result)
        return result


class SumCalculation:

    def calculate(self, input_data: SumCalculationInput):
        self.input_data = input_data

        result = input_data.X + input_data.Y

        return SumCalculationResult(Z=result)
