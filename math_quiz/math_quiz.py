import random

def generate_random_integer(min_value: int, max_value: int) -> int:
    """
    Generates a random integer within a specified range.

    Args:
        min_value (int): The minimum value of the random integer.
        max_value (int): The maximum value of the random integer.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def choose_random_operator() -> str:
    """
    Selects a random arithmetic operator from the options: +, -, *.

    Returns:
        str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])

def generate_problem_and_answer(num1: int, num2: int, operator: str) -> tuple:
    """
    Creates a math problem and calculates its correct answer based on the given operator.

    Args:
        num1 (int): The first operand in the math problem.
        num2 (int): The second operand in the math problem.
        operator (str): An arithmetic operator, which can be '+', '-', or '*'.

    Returns:
        tuple: A tuple containing:
            - str: The math problem in string form (e.g., "3 + 4").
            - int: The correct answer to the math problem.
    """
    problem_str = f"{num1} {operator} {num2}"

    # Determine the answer based on the operator
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    else:
        raise ValueError("Invalid operator. Operator must be one of '+', '-', or '*'.")

    return problem_str, correct_answer

def math_quiz():
    """
    Runs a math quiz game, presenting the user with randomly generated math problems.
    The user's answers are evaluated, and the score is tracked.

    Instructions:
    - The user is presented with a math problem and is prompted to input an answer.
    - Correct answers score points, while incorrect answers display the correct solution.
    """
    score = 0
    total_questions = 3  # Define the total number of questions

    print("Welcome to the Math Quiz Game!")
    print("Solve the math problems presented to you.")

    for _ in range(total_questions):
        # Generate random numbers and operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 10)
        operator = choose_random_operator()

        # Generate the problem and its correct answer
        problem, correct_answer = generate_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Get and validate user input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # Skip to the next question if input is invalid

        # Check if the answer is correct and update the score
        if user_answer == correct_answer:
            print("Correct! You've earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
