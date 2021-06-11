#!/usr/bin/env python
import random
import prompt
from brain_games.scripts.brain_games import flow, main as main_, format_answer


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
        return ['True', ]
    else:
        return ['False', format_answer(answer), format_answer(result)]


def main():
    user = main_()
    greetings = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    flow(rand_numb, greetings, user)


if __name__ == '__main__':
    main()
