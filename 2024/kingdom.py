#!/bin/python3

import math
import os
import random
import re
import sys

def divide(n, roads, p):
    # p is the number of cities to select from n 
    # such that each of the p is atleast connected to one other city
    # roads is a list of roads connecting the cities
    # create a hash table where each city is a key and the value is a list of cities it is connected to
    connected_cities = {}
    for road in roads:
        if road[0] not in connected_cities:
            connected_cities[road[0]] = [road[1]]
        else:
            connected_cities[road[0]].append(road[1])
        if road[1] not in connected_cities:
            connected_cities[road[1]] = [road[0]]
        else:
            connected_cities[road[1]].append(road[0])

    # create a list of cities that are connected to atleast one other city
    number_of_connected_cities = 0
    for city in connected_cities:
    
    # return the number of ways in which p cities can be selected from n cities
    return (math.factorial(n) // (math.factorial(p) * math.factorial(n - p))) - number_of_connected_cities

def kingdomDivision(n, roads):
    possibilities = 2

    # in the start all the cities are in red kingdom
    # we add the ways in which blue kingdom can be formed
    for i in range(2, n - 1):
        possibilities  = (possibilities +  divide(n, roads, i)) % (10 ** 9 + 7)

    return possibilities

if __name__ == '__main__':
    n = 5
    roads = [
        [1, 2],
        [1, 3],
        [3, 4],
        [3, 5]
    ]

    result = kingdomDivision(n, roads)
    print(result)