import unittest

from ddd.source.hexagonal_architecture_idea_example._10_add_customer_notifier.app import (
    RedisIdeaRepository,
    RateIdeaUseCase,
    RateIdeaRequest
)


class TestRedisRepositiry(unittest.TestCase):

    def test_(self):
        client = RedisClient(attrdict={
            '1': dict(
                title='TITLE',
                description='DESCR',
                rating=4,
                votes=0,
                email='xxx@xxx.com'
            )
        })
        repository = RedisIdeaRepository(client)
        use_case = RateIdeaUseCase(repository)
        input_data = RateIdeaRequest('1', 1)

        use_case.execute(input_data)

        idea = repository.find_by_id('1')
        self.assertEqual(5, idea.rating)


class RedisClient:

    def __init__(self, attrdict):
        self.attrdict = attrdict

    def hmget(self, id_, key):
        record = self.attrdict.get(id_)
        value = record.get(key)
        encoded = value.encode() if isinstance(value, str) else value
        result = [encoded]
        return result

    def hmset(self, id_, record: dict):
        self.attrdict[id_] = record
