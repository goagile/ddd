import unittest


class Test(unittest.TestCase):

    def test_simple_notifier(self):
        logger = Logger()
        n = Notifier()

        n.notify('Hello')

        self.assertTrue('Hello', n.message)
        self.assertEqual([], logger.messages)

    def test_decorated_notifier(self):
        logger = Logger()
        n = NotifierDecorator(Notifier(), logger)

        n.notify('Hello')

        self.assertTrue('Hello', n.message)
        self.assertEqual(['Hello'], logger.messages)


class Notifier:

    message = ''

    def notify(self, message):
        self.message = message


class NotifierDecorator:

    def __init__(self, notifier, logger):
        self.notifier = notifier
        self.logger = logger

    @property
    def message(self):
        return self.notifier.message

    def notify(self, message):
        self.notifier.notify(message)
        self.logger.log(message)


class Logger:

    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)


if __name__ == '__main__':
    unittest.main()