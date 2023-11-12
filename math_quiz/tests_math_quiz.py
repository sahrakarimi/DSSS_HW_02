import unittest

from math_quiz import get_random_integer, get_random_operator, apply_operator

class TestMathGame(unittest.TestCase):
    """
    It is a test for math game whether it is working properly.
    This is an extension of the :class:`unittest.TestCase` class.
    """

    def test_get_random_integer(self):
        """
        Test if random numbers generated are within the specified range
        """
       
        min_val = 1
        max_val = 10

        # Test a large number of random values
        number_of_samples = 1000

        for _ in range(number_of_samples):  
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def get_random_operator(self):
        # TODO
        pass

    def apply_operator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()
