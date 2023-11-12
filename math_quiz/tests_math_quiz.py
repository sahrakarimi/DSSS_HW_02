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

    def test_get_random_operator(self):
        """
        Test if random operator generated are from ['+', '*', '-']
        """
        # Test a large number of times and check if it returns a valid operator
        number_of_samples = 100

        for _ in range(number_of_samples):  
            operator = get_random_operator ()
            self.assertTrue(operator in ['+', '*', '-'])

    def test_apply_operator(self):
            test_cases = [

                (5, 2, '+', '5 + 2', 7),     
                (4, -2, '+', '4 + -2', 2),
                (-2,-3, '+', '-2 + -3', -5),
                (3, 5, '*', '3 * 5', 15),
                (-5, 4, '*', '-5 * 4', -20),
                (-2, -3, '*', '-2 * -3', 6),
                (10, 5, '-', '10 - 5', 5),
                (2, -8, '-', '2 - -8', 10),
                (-1,-2, '-', '-1 - -2', 1)
            ]

            for num_1, num_2, operator, expected_problem, expected_answer in test_cases:

                (result_equation, result) = apply_operator(num_1, num_2, operator)
                self.assertEqual(result_equation, expected_problem)
                self.assertEqual(result, expected_answer)

if __name__ == "__main__":
    unittest.main()
