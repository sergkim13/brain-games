import prompt

score_to_win = 3


def greeter():
    print('Welcome to the Brain Games!')


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def print_game_task(game_task):
    print(game_task)


def start_game(game, user_name):
    score = 0
    while score < score_to_win:
        question, correct_answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            break
    if score == 3:
        print(f'Congratulations, {user_name}!')
