import random


def get_random_integer(min, max):
    """
    Random integer.
    """
    random_int = random.randint(min, max)

    return random_int

def get_random_operator():

    return random.choice(['+', '-', '*'])


def apply_operator(operand_1, operand_2, operator):

    printable_equation = f"{operand_1} {operator} {operand_2}"

    if operator == '-': 
        result = operand_1 - operand_2
    elif operator == '+': 
        result = operand_1 + operand_2
    else: 
        result = operand_1 * operand_2

    return printable_equation, result

def math_quiz():
    
    score = 0
    question_times = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(question_times):

        operand_1 = get_random_integer(1, 10)
        operand_2 = get_random_integer(1, 5)
        operator = get_random_operator()

        (problem, answer) = apply_operator(operand_1, operand_2, operator)

        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{question_times}")

if __name__ == "__main__":
    math_quiz()
