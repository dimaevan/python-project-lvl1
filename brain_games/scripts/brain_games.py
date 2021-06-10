#!/usr/bin/env python
from brain_games.scripts.cli import welcome_user
from brain_games.scripts.brain_even import even


def main():
    print("Welcome to the Brain Games!")
    x = welcome_user()
    print('Hello, {0}'.format(x))
    print(even(x))


if __name__ == '__main__':
    main()
