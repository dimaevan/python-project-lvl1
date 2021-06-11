#!/usr/bin/env python
import random
import prompt
from brain_games.scripts.brain_games import main as main_, flow


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def even():
    number = random.randint(1, 100)
    print('Question: {0}'.format(number))
    answer = prompt.string('Your answer: ')
    if is_even(number):
        if answer == 'yes':
            return ['True', ]
        else:
            return ['False', "'no'", "'yes'"]
    else:
        if answer == 'yes':
            return ['False', "'yes'", "'no'"]
        else:
            return ['True', ]


def main():
    user = main_()
    greetings = 'Answer "yes" if the number is even, otherwise answer "no".'
    flow(even, greetings, user)


if __name__ == '__main__':
    main()
