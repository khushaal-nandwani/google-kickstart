#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMinimumCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMinimumCost(arr):
    # Write your code here
    cost = 0
    n = len(arr)

    for i in range(n):
        try:
            cost += abs(arr[i+1] - arr[i])
        except IndexError:
            break
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = findMinimumCost(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
