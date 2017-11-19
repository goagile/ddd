import unittest

from ddd.source.hexagonal_architecture._8_testing.app import (
    RedisIdeaRepository,
    RateIdeaUseCase,
    RateIdeaRequest,
    RepositoryNotAvailableException
)


class TestCase(unittest.TestCase):

    def test_when_repository_not_available_an_exception_should_be_raised(self):
        repository = RedisIdeaRepository()
        use_case = RateIdeaUseCase(repository)
        input_data = RateIdeaRequest('333', 4)

        with self.assertRaises(RepositoryNotAvailableException):
            use_case.execute(input_data)
