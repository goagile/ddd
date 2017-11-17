import unittest


HOME_PHONE_NUMBER = '4-29-62'
WORK_PHONE_NUMBER = '4-67-68'


class TestPhoneBook(unittest.TestCase):
    """
        Клиент имеет Рабочий, Домашний и Мобильный телефон
    """

    def test_set_work_phone(self):
        book = PhoneBook()

        book.set_work_phone(WORK_PHONE_NUMBER)

        self.assertEqual(WORK_PHONE_NUMBER, str(book.work_phone))

    def test_set_home_phone(self):
        book = PhoneBook()

        book.set_home_phone(HOME_PHONE_NUMBER)

        self.assertEqual(HOME_PHONE_NUMBER, str(book.home_phone))


class TestPhone(unittest.TestCase):

    def test_work_phone(self):
        work_phone = WorkPhone(WORK_PHONE_NUMBER)

        self.assertEqual(WORK_PHONE_NUMBER, str(work_phone))

    def test_home_phone(self):
        home_phone = HomePhone(HOME_PHONE_NUMBER)

        self.assertEqual(HOME_PHONE_NUMBER, str(home_phone))

    def test_equal(self):
        phone1 = Phone(HOME_PHONE_NUMBER)
        phone2 = Phone(HOME_PHONE_NUMBER)
        self.assertEqual(phone1, phone2)


class Phone:

    def __init__(self, phone_number: str):
        self.__phone_number = phone_number

    @property
    def phone_number(self):
        return self.__phone_number

    def __str__(self):
        return '{}'.format(self.__phone_number)

    def __eq__(self, other):
        return bool(self.phone_number == other.phone_number)


class WorkPhone(Phone):

    def __init__(self, work_phone_number: str):
        super().__init__(work_phone_number)


class HomePhone(Phone):

    def __init__(self, home_phone_number: str):
        super().__init__(home_phone_number)


class PhoneBook:

    def __init__(self):
        self.__work_phone = None
        self.__home_phone = None

    @property
    def work_phone(self):
        return self.__work_phone

    @property
    def home_phone(self):
        return self.__home_phone

    def set_work_phone(self, work_phone_number: str):
        self.__work_phone = WorkPhone(work_phone_number)

    def set_home_phone(self, home_phone_number: str):
        self.__home_phone = HomePhone(home_phone_number)
