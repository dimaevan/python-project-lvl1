#!/usr/bin/env python
import random
import prompt
from brain_games.scripts.brain_games import flow, main as main_


def divider(num):
    array_divider = []
    for _ in range(1, num + 1):
        if num % _ == 0:
            array_divider.append(_)
    return set(array_divider)


def nod(first_num, second_num):
    dividers_first = divider(first_num)
    dividers_second = divider(second_num)
    nod_of_sets = dividers_first.intersection(dividers_second)
    if len(nod_of_sets) == 0:
        return 0
    else:
        return max(nod_of_sets)


def gcd():
    var_1 = random.randint(0, 100)
    var_2 = random.randint(0, 100)
    print('Question: {0} {1}'.format(var_1, var_2))
    result = int(nod(var_1, var_2))
    answer = prompt.integer('Your answer: ')
    if result == answer:
        return ['True', answer, ]
    else:
        return ['False', answer, result]


def main():
    user = main_()
    greeting = 'Find the greatest common divisor of given numbers.'
    flow(gcd, greeting, user)


if __name__ == '__main__':
    main()
