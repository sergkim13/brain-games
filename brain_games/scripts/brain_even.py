#!/usr/bin/env python3
from brain_games.games.engine import (
    greeter, welcome_user, print_game_task, start_game
)
from brain_games.games.even_core import game_task, get_question


def main():
    greeter()
    user_name = welcome_user()
    print_game_task(game_task)
    start_game(get_question, user_name)


if __name__ == '__main__':
    main()
