#!/usr/bin/env python
import random
import prompt
from . import brain_games


def is_simple(num):
    for i in range(2, num):
        if num % i == 0:
            return 'no'
    else:
        return 'yes'


def rand_numb():
    x = random.randint(1, 100)
    print('Question: {0}'.format(x))
    answer = prompt.string('Your answer: ')
    result = is_simple(x)
    if answer == result:
        return ['True', answer, ]
    else:
        return ['False', answer, result]


def main():
    user = brain_games.main()
    greetings = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    brain_games.flow(rand_numb, greetings, user)


if __name__ == '__main__':
    main()
