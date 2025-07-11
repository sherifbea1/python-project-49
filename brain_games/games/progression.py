import random

RULES = 'What number is missing in the progression?'


def get_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = 10
    hidden_index = random.randint(0, length - 1)

    progression = [str(start + step * i) for i in range(length)]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)

    return question, correct_answer