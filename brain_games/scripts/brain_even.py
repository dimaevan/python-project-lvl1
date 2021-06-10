#!/usr/bin/env python
import random
import prompt
from brain_games.scripts.cli import welcome_user


def even(user):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    numbers_of_right_answer = 0
    name = user
    while numbers_of_right_answer < 3:
        number = random.randint(1, 100)
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        if is_even(number):
            if answer == 'yes':
                print('Correct!')
                numbers_of_right_answer += 1
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print("Let's try again, {0}".format(name))
        else:
            if answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print("Let's try again, {0}".format(name))
            else:
                print('Correct!')
                numbers_of_right_answer += 1
    if numbers_of_right_answer == 3:
        return 'Congratulations, {0}'.format(name)


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def main():
    print("Welcome to the Brain Games!")
    x = welcome_user()
    print('Hello, {0}'.format(x))
    print(even(x))


if __name__ == '__main__':
    main()
