import random

def get_random_integer(min, max):
    """
    Produce a random integer number in range min and max.

    :param min: The min value 
    :type min: int
    :param max: The max value
    :type max: int
    :return: A random integer number between min and max
    :rtype: int
    """
    random_int = random.randint(min, max)

    return random_int

def get_random_operator():
    """
    Produce a random arithmetic operator from (+ , -, *).

    :return: A random arithmetic operator (addition, subtraction, multiplication)
    :rtype: str (length-1)
    """
    random_operator = random.choice(['+', '-', '*'])

    return random_operator


def apply_operator(operand_1, operand_2, operator):
    """
    Calculate the arithmetic operation of two integer numbers.

    :param operand_1: The first number
    :type operand_1: int
    :param operand_2: The second number
    :type operand_2: int
    :param operator: The random arithmetic operator
    :type operator: str
    :return: The equation string and result of arithmetic operation 
    :rtype: tuple (str, int)
    """

    printable_equation = f"{operand_1} {operator} {operand_2}"

    # Calculate the result depending on the operator
    if operator == '-': 
        result = operand_1 - operand_2
    elif operator == '+': 
        result = operand_1 + operand_2
    else:
        result = operand_1 * operand_2

    return printable_equation, result

def math_quiz():
    """
    It is a math game and ask the user a random math question for 
    3-times and prints the calculated final score.
    """

    score = 0
    question_times = 3    # TODO: make this as a function argument

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Repeat the game for 'question_times' times
    for _ in range(question_times):

        operand_1 = get_random_integer(1, 10)
        operand_2 = get_random_integer(1, 5)
        operator = get_random_operator()

        (problem, answer) = apply_operator(operand_1, operand_2, operator)

        # Print the question and wait to receive response from the user
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except:
            print("Invalid answer!! You lost the point. Valid answers are integer.")
            continue

        # Validate the answer and update the score
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{question_times}")

if __name__ == "__main__":
    math_quiz()
