import unittest

from ddd.source.hexagonal_architecture._8_testing.app import (
    RedisIdeaRepository,
    RateIdeaUseCase,
    RateIdeaRequest,
    RepositoryNotAvailableException,
    IdeaDoesNotExistException,
    IdeaRepository,
    Idea
)


class TestCase(unittest.TestCase):

    def test_when_repository_not_available_an_exception_should_be_raised(self):
        repository = NotAvailableRepository()
        use_case = RateIdeaUseCase(repository)
        input_data = RateIdeaRequest('1', 4)

        with self.assertRaises(RepositoryNotAvailableException):
            use_case.execute(input_data)

    def test_when_idea_does_not_exist_an_exception_should_be_raised(self):
        repository = EmptyRepository()
        use_case = RateIdeaUseCase(repository)
        input_data = RateIdeaRequest('1', 4)

        with self.assertRaises(IdeaDoesNotExistException):
            use_case.execute(input_data)


class NotAvailableRepository(IdeaRepository):

    def find_by_id(self, idea_id: str):
        raise RepositoryNotAvailableException()

    def update(self, idea: Idea):
        raise RepositoryNotAvailableException()


class EmptyRepository(IdeaRepository):

    def find_by_id(self, idea_id: str):
        pass

    def update(self, idea: Idea):
        pass
