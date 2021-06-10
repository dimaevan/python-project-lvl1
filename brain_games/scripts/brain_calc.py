#!/usr/bin/env python
import random
import prompt
from brain_games.scripts.cli import welcome_user


def calc(user):
    name_user = user
    var_1 = random.randint(0, 100)
    var_2 = random.randint(0, 100)
    operation = random.choice(['+', '-', '*'])
    print(var_1, operation, var_2)
    if operation == '+':
        result = var_1 + var_2
    elif operation == '-':
        result = var_1 - var_2
    else:
        result = var_1 * var_2
    answer_user = prompt.integer('Your answer: ')
    if answer_user == result:
        print('Correct!')
        return True
    else:
        print('{0} is wrong answer ;(. '
              'Correct answer was {1}.'.format(answer_user, result))
        print("Let's try again, {0}!".format(name_user))
        return False


def main():
    print("Welcome to the Brain Games!")
    user = welcome_user()
    print('Hello, {}'.format(user))
    right_answers = 0
    while right_answers < 3:
        if calc(user):
            right_answers += 1
    print('Congratulations, {}!'.format(user))


if __name__ == '__main__':
    main()
