import sys


def average(a: int, b: int) -> float:
    return (a + b) / 2

test_cases = int(sys.stdin.readline())

for j in range(test_cases):

    row1 = sys.stdin.readline().split()
    for i in range(3):
        row1[i] = int(row1[i])

    row2 = sys.stdin.readline().split()
    for i in range(2):
        row2[i] = int(row2[i])

    row3 = sys.stdin.readline().split()
    for i in range(3):
        row3[i] = int(row3[i])

    G00  = row1[0]
    G01 = row1[1]
    G02 = row1[2]
    G10 = row2[0]
    G12 = row2[1]
    G20 = row3[0]
    G21 = row3[1]
    G22 = row3[2]

    # check for borders
    border_count = 0

    x = average(G02, G22)
    if G12 == x:
        border_count += 1

    x = average(G20, G22)
    if G21 == x:
        border_count += 1

    x = average(G00, G20)
    if G10 == x:
        border_count += 1

    x = average(G02, G00)
    if G01 == x:
        border_count += 1

    count: dict
    count = {0: 0}    # key is number, value is count

    x = average(G00, G22)
    if (x == int(x)):
        if x not in count.keys():
            count[x] = 1
        else:
            count[x] += 1

    x = average(G10, G12)
    if (x == int(x)):
        if x not in count.keys():
            count[x] = 1
        else:
            count[x] += 1

    x = average(G20, G02)
    if (x == int(x)):
        if x not in count.keys():
            count[x] = 1
        else:
            count[x] += 1

    x = average(G01, G21)
    if (x == int(x)):
        if x not in count.keys():
            count[x] = 1
        else:
            count[x] += 1

    values_of_Count = count.values()
    print('Case', f'#{j+1}:', max(values_of_Count) + border_count)


