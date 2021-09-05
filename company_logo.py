#!/bin/python3

import math
import os
import random
import re
import sys


def finder(s: str):
    max_1 = ('a', 0)
    max_2 = ('a', 0)
    max_3 = ('a', 0)
    used_letters = {}
    for letter in s:
        if letter not in used_letters:
            used_letters[letter] = 1
        else:
            used_letters[letter] += 1

    for key, value in used_letters.items():
        if value >= max_1[1]:
            if value == max_1[1]:
                if max_1[0] > key:
                    # agar max_1 ka letter chota hai toh swap
                    max_1, max_2, max_3 = (key, value), max_1, max_2
                    continue
            else:
                max_1, max_2, max_3 = (key, value), max_1, max_2
                continue
        if value >= max_2[1]:
            if value == max_2[1]:
                letter_war = max_2[0] > key
                if letter_war:
                    max_2, max_3 = (key, value), max_2
                    continue
            else:
                max_2, max_3 = (key, value), max_2
                continue
        if value >= max_3[1]:
            if value == max_3[1]:
                letter_war = max_3[0] > key
                if letter_war:
                    max_3 = (key, value)
                    continue
            else:
                max_3 = key, value
    return [max_1, max_2, max_3]


if __name__ == '__main__':
    s = input()
    values = finder(s)
    for tup in values:
        print(tup[0], tup[1])
