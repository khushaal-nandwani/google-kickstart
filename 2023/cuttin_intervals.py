import sys
from collections import deque

test_number = int(sys.stdin.readline())
for test in range(test_number):
    n_and_c = sys.stdin.readline().split()
    N = int(n_and_c[0])
    C = int(n_and_c[1])

    total_intervals = N
    intervals = []

    first_interval = sys.stdin.readline().split()
    interval = (int(first_interval[0]), int(first_interval[1]))
    intervals.append(interval)

    for other_interval in range(N - 1):
        interval_scanned = sys.stdin.readline().split()
        interval = (int(interval_scanned[0]), int(interval_scanned[1]))
        x = interval[0]
        y = interval[1]
        intervals.append(interval)

    min_x = min(intervals)[0]
    max_y = max(intervals)[1]

    added = [0]
    added_count = 0
    for i in range(min_x + 1, max_y):
        potential_addition = 0
        for interval in intervals:
            if interval[0] < i < interval[1]:
                potential_addition += 1
        if potential_addition >= added[0]:
            if added_count == C:
                added = added[1:]
                total_intervals += potential_addition
                added.append(potential_addition)
            total_intervals += potential_addition
            added_count += 1
    print('Case', f'#{test + 1}:', total_intervals)






