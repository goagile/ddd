import unittest

from ddd.source.hexagonal_architecture_idea_example._10_add_customer_notifier.app import (
    RedisIdeaRepository,
    RateIdeaUseCase,
    RateIdeaRequest,
    RepositoryNotAvailableException,
    IdeaDoesNotExistException,
    IdeaRepository,
    Idea,
    AuthorNotifier
)


class TestNotifyAuthor(unittest.TestCase):

    def test_(self):
        repository = OneIdeaRepository()
        notifier = OneAuthorNotifier()
        use_case = RateIdeaUseCase(repository, notifier)
        input_data = RateIdeaRequest('1', 1)

        result = use_case.execute(input_data)

        actual = result.idea.rating
        self.assertEqual(5, actual)
        self.assertTrue(notifier.is_notified)


class OneAuthorNotifier(AuthorNotifier):

    is_notified = False

    def notify(self, author: str):
        self.is_notified = True


class OneIdeaRepository(IdeaRepository):

    update_called = False

    def find_by_id(self, idea_id: str):
        idea = Idea()
        idea.idea_id = idea_id
        idea.title = 'Title'
        idea.description = 'Description'
        idea.rating = 4
        idea.votes = 0
        idea.email = 'xxx@xxx.com'

        return idea

    def update(self, idea: Idea):
        self.update_called = True
