from random import randint, choice


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def isprime(value):
    value = int(value)
    if value < 2:
        return False
    for i in range(2, value // 2 + 1):
        if value % i == 0:
            return False
    return True

def get_question():
    question = randint(1, 100)
    if isprime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer