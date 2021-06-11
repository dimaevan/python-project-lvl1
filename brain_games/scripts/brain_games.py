#!/usr/bin/env python
from brain_games.scripts.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print('Hello, {0}'.format(user_name))
    return user_name


def flow(func, greeting, user):
    print(greeting)
    numbers_of_correct_answer = 0
    while numbers_of_correct_answer < 3:
        this_func = func()
        if this_func[0] == 'True':
            print('Correct!')
            numbers_of_correct_answer += 1
        elif this_func[0] == 'False':
            print('"{0}" is wrong answer ;(. '
                  'Correct answer was "{1}".'.format(this_func[1],
                                                     this_func[2]))
            print("Let's try again, {0}!".format(user))
            break
    if numbers_of_correct_answer == 3:
        print('Congratulations, {0}!'.format(user))


if __name__ == '__main__':
    main()
