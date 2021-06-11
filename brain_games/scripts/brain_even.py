#!/usr/bin/env python
import random
import prompt
from . import brain_games


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
            return ['True', answer, ]
        else:
            return ['False', answer, 'yes']
    else:
        if answer == 'yes':
            return ['False', 'yes', 'no']
        else:
            return ['True', answer, ]


def main():
    user = brain_games.main()
    greetings = 'Answer "yes" if the number is even, otherwise answer "no".'
    brain_games.flow(even, greetings, user)


if __name__ == '__main__':
    main()
