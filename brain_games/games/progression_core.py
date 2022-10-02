from random import randint, choice


game_task = 'What number is missing in the progression?'


def get_question():
    progression = []
    progression_length = randint(6, 15)
    progression_start = randint(1, 20)
    progression_step = randint(1,5)
    for _ in range(progression_length):
        progression.append(progression_start + _ * progression_step)
    picked_number = choice(progression)
    progression[progression.index(picked_number)] = '..'
    question = ' '.join(map(str, progression))
    correct_answer = str(picked_number)
    return question, correct_answer
