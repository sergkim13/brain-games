import prompt
from random import randint


def calc():
    correct_answer_counter = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    while correct_answer_counter < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        # тут логика игры
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            correct_answer_counter += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    if correct_answer_counter == 3:
        print(f'Congratulations, {name}!')
