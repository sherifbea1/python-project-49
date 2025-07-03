import random

RULES = "What is the result of the expression?"

def get_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])

    question = f"{num1} {operation} {num2}"

    if operation == '+':
        correct_answer = str(num1 + num2)
    elif operation == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)

    return question, correct_answer
