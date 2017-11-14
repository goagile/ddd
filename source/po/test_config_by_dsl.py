import unittest

from nilsson.start_examples.po.config_by_dsl import StateMachineConfig


class Test(unittest.TestCase):

    def test_states(self):
        class Config(StateMachineConfig):
            def configure(self, states, events, when):
                states.waiting_msg_id
                states.waiting_msg_str

        expected = ['waiting_msg_id', 'waiting_msg_str']
        config = Config()
        config.run()

        result = config.states_builder.states

        self.assertEqual(expected, result)

    def test_events(self):
        class Config(StateMachineConfig):
            def configure(self, states, events, when):
                events.msg_id_finded
                events.msg_str_finded

        expected = ['msg_id_finded', 'msg_str_finded']
        config = Config()
        config.run()

        result = config.events_builder.events

        self.assertEqual(expected, result)

    def test_transitions(self):
        class Config(StateMachineConfig):
            def configure(self, states, events, when):
                states.waiting_msg_id
                states.waiting_msg_str

                events.msg_id_finded
                events.msg_str_finded

                when.msg_id_finded.transit.waiting_msg_id.waiting_msg_str

        expected_states = ['waiting_msg_id', 'waiting_msg_str']
        expected_events = ['msg_id_finded', 'msg_str_finded']

        config = Config()
        config.run()

        self.assertEqual(expected_states, config.states_builder.states)
        self.assertEqual(expected_events, config.events_builder.events)
