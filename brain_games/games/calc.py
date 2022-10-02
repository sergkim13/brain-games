from random import randint, choice
import operator


game_task = 'What is the result of the expression?'
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}

def get_question():
    number1 = randint(1, 10)
    number2 = randint(1, 40)
    random_operator = choice(list(OPERATORS))
    question = f'{number1} {random_operator} {number2}'
    correct_answer = str(OPERATORS[random_operator](number1, number2))
    return question, correct_answer

