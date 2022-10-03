#!/usr/bin/env python3
from brain_games.games.cli import welcome_user


def greeter():
    print('Welcome to the Brain Games!')


def main():
    greeter()
    welcome_user()


if __name__ == '__main__':
    main()
