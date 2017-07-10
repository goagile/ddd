import unittest

from nilsson.orders_and_customers.application_layer import CustomerRepository, FakeWorkspace
from nilsson.orders_and_customers.domain_layer import Customer

workspace = FakeWorkspace()
repository = CustomerRepository(workspace)


class Test(unittest.TestCase):

    @unittest.skip('not realized')
    def test_can_save_2_customers(self):
        no_of_customers_before = self.get_number_of_stored_customers()
        customer_1 = Customer()
        customer_1.name = 'Volvo'
        customer_repository.add(customer_1)
        customer_2 = Customer()
        customer_2.name = 'Saab'
        customer_repository.add(customer_2)

        self.assertEqual(no_of_customers_before, self.get_number_of_stored_customers())

        self.ws.persist_all()

        self.assertEqual(2 + no_of_customers_before, self.get_number_of_stored_customers())

    @unittest.skip('not realized')
    def test_can_add_customer(self):
        customer = Customer()
        customer.name = 'Volvo'
        customer.key = 42
        repository.add(customer)
        workspace.persist_all()
        workspace.clean()

        customer_2 = repository.get_by_key(customer.key)

        self.assertEqual(customer.name, customer_2.name)

        repository.delete()
        workspace.persist_all()
