#!/usr/bin/env python
import random
import prompt
from brain_games.scripts.brain_games import flow, main as main_


def calc():
    var_1, var_2 = random.randint(0, 100), random.randint(0, 100)
    operation = random.choice(['+', '-', '*'])
    print('Question: ', var_1, operation, var_2)
    if operation == '+':
        result = var_1 + var_2
    elif operation == '-':
        result = var_1 - var_2
    else:
        result = var_1 * var_2
    answer = prompt.integer('Your answer: ')
    if answer == result:
        return ['True', answer]
    else:
        return ['False', answer, result]


def main():
    user = main_()
    flow(calc, 'What is the result of the expression?', user)


if __name__ == '__main__':
    main()
