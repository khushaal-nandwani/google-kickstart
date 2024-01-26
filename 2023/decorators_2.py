from itertools import groupby
import operator
from typing import Callable


def person_lister(f: Callable):
    def inner(people):
        for x in people:
            x[2] = int(x[2])
        people.sort(key=operator.itemgetter(2))
        for i in range(len(people)):
            people[i] = f(people[i])
        return people

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + \
           person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    haha = people[:]
    print(*name_format(people), sep='\n')
