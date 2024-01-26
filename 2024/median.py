#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappush, heappop, heapify

def runningMedian(a):
    small_heap = []  # heap containing smaller elements max heap
    heapify(small_heap) 
    large_heap = []  # heap containing larger elements min heap
    heapify(large_heap)

    median: float
    result = []

    even = True

    if len(a) >= 1:
        result.append(float(a[0]))
    
    if len(a) >= 2:
        if a[0] > a[1]:
            heappush(large_heap, a[0])
            heappush(small_heap, - a[1])
        else:
            heappush(large_heap, a[1])
            heappush(small_heap, - a[0])
        median = float((a[0] + a[1])/2)
        result.append(median)

    for i in range(2, len(a)):   
        element = a[i]

        # insertion
        if element > -min(small_heap):
            heappush(large_heap, element)
        else:
            heappush(small_heap,- element)
  
        
        # balance if they got unbalanced
        if abs(len(small_heap) - len(large_heap)) > 1:
            if len(small_heap) > len(large_heap):
                element_popped = - heappop(small_heap)
                heappush(large_heap, element_popped)
            else:
                element_popped =  - heappop(large_heap)
                heappush(small_heap, element_popped)
        even = not even
        if even:
            # median is avg of top heap elements
            result.append(float((float(large_heap[0]) + float(-small_heap[0])) / 2))
        else:
            # median is the top element of bigger heap
            if len(small_heap) > len(large_heap):
                result.append(float(-small_heap[0]))
            else:
                result.append(float((large_heap[0])))

    return result

if __name__ == '__main__':

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    print('\n'.join(map(str, result)))
    print('\n')

