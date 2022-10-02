from random import randint
import math

game_task = 'Find the greatest common divisor of given numbers.'


def get_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'{number1} {number2}'
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer
