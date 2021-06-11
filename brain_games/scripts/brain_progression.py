#!/usr/bin/env python
import random
import prompt
from . import brain_games


def make_progression():
    start_pos = random.randint(0, 10)
    num_progress = random.randint(0, 10)
    my_progression = []
    for _ in range(0, 10):
        new_pos = start_pos + num_progress
        my_progression.append(new_pos)
        start_pos = new_pos
    return my_progression


def delete_and_answer():
    arithmetic_progress = make_progression()
    i = random.choice(arithmetic_progress)
    index_hidden = arithmetic_progress.index(i)
    result = arithmetic_progress[index_hidden]
    arithmetic_progress[index_hidden] = '..'
    print('Question: ', end='')
    for x in arithmetic_progress:
        print(x, end=' ')
    print()
    answer = prompt.integer('Your answer: ')
    if answer == result:
        return ['True', ]
    else:
        return ['False', answer, result]


def main():
    user = brain_games.main()
    greetings = 'What number is missing in the progression?'
    brain_games.flow(delete_and_answer, greetings, user)


if __name__ == '__main__':
    main()
