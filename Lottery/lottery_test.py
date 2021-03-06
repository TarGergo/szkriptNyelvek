import unittest
import numpy as np
from lottery import generate_lottery_ticket


class TestLottery(unittest.TestCase):

   def test_generate_lottery_ticket_should_have_exactly_five_numbers(self):
        LOTTERY_TICKET_EXPECTED_SIZE = 5
        actual = generate_lottery_ticket()
        self.assertTrue(isinstance(actual, np.ndarray))
        self.assertEqual(len(actual), LOTTERY_TICKET_EXPECTED_SIZE)

   def test_generate_lottery_ticket_should_be_ordered(self):
        actual = generate_lottery_ticket()
        for i in range(1, len(actual)):
             self.assertTrue(actual[i-1] < actual[i])

   def test_generate_lottery_ticket_should_each_number_within_one_and_ninety(self):
        MINIMUM_VALUE = 1
        MAXIMUM_VALUE = 90
        actual = generate_lottery_ticket()
        self.assertTrue(np.logical_and(MINIMUM_VALUE <= actual, actual <= MAXIMUM_VALUE).all())