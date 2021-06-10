#!/usr/bin/env python
import random
import prompt
from brain_games.scripts.cli import welcome_user


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


def gcd(user_name):
    user = user_name
    var_1 = random.randint(0, 100)
    var_2 = random.randint(0, 100)
    print('Question: {0} {1}'.format(var_1, var_2))
    this_nod = int(nod(var_1, var_2))
    answer = prompt.integer('Your answer: ')
    if this_nod == answer:
        print('Correct!')
        return True
    else:
        print('{0} is wrong answer ;(. '
              'Correct answer was {1}.'.format(answer, this_nod))
        print("Let's try again, {0}!".format(user))
        return False


def main():
    print("Welcome to the Brain Games!")
    user = welcome_user()
    print('Hello, {0}'.format(user))
    print('Find the greatest common divisor of given numbers.')
    gcd(user)
    right_answers = 0
    while right_answers < 3:
        if gcd(user):
            right_answers += 1
    print('Congratulations, {}!'.format(user))


if __name__ == '__main__':
    main()
