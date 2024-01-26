#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    if len(A) == 1:
        if A[0] >= k:
            return 0
        else:
            return -1
    steps = 0
    # create a min heap O(nlogn)
    heap = []
    heapq.heapify(heap)
    for num in A:
        heapq.heappush(heap, num)
    while heap[0] < k:
        if (len(heap) == 1):
            if heap[0] >= k:
                return steps
            else:
                return -1
            
        # pop two things
        least = heapq.heappop(heap)
        second_least = heapq.heappop(heap)
        # add them together
        print(least, second_least)
        new_cookie = least + (2 * second_least)
        print(new_cookie)
        steps += 1
        # do the math and innsert back into the heap
        heapq.heappush(heap, new_cookie)
    return steps

if __name__ == '__main__':
    # n = 2
    # k = 10
    # A = [0, 1]
    # print(cookies(k, A))
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
