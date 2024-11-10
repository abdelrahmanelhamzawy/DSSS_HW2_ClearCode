import unittest
from math_quiz import generate_random_integer, choose_random_operator, generate_problem_and_answer

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_random_operator(self):
        # Test if the random operator returned is one of the valid operators
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test many times to ensure randomness
            operator = choose_random_operator()
            self.assertIn(operator, valid_operators)

    def test_generate_problem_and_answer(self):
        # Test for various cases with different operators
        test_cases = [
            (5, 2, '+', '5 + 2', 7),  # 5 + 2 should give the problem '5 + 2' and answer 7
            (7, 3, '-', '7 - 3', 4),  # 7 - 3 should give the problem '7 - 3' and answer 4
            (6, 4, '*', '6 * 4', 24), # 6 * 4 should give the problem '6 * 4' and answer 24
            (10, 5, '+', '10 + 5', 15),  # 10 + 5 should give the problem '10 + 5' and answer 15
            (8, 2, '-', '8 - 2', 6),  # 8 - 2 should give the problem '8 - 2' and answer 6
            (9, 3, '*', '9 * 3', 27)  # 9 * 3 should give the problem '9 * 3' and answer 27
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem_and_answer(num1, num2, operator)
            # Check if the problem generated is correct
            self.assertEqual(problem, expected_problem)
            # Check if the calculated answer is correct
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
