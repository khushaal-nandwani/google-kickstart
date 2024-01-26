from random import randint


def find_position(A, target: object, count) -> int:
    j = 0
    for i in range(len(A)):
        j += 1
        if A[i] == target:
            return j
    return j


def encode(L, M, k) -> int:
    count = 0
    result = 0
    for i in range(len(L)):
        count += 1
        if L[i] == k:
            result += M[i]
        else:
            count += find_position(M, L[i], count)
            result += 1
    return count

range_for_L = 3
range_for_M = 40
no_of_entries = 0 # kitne baar encode kiya
total_steps = 0
while no_of_entries < 10000:
    # initializing L and M
    L = [randint(0, 9) for i in range(1, range_for_L + 1)]
    M = [randint(0, 9) for x in range(1, range_for_M + 1)]
    k = randint(0, 9)

    total_steps += encode(L, M, k)
    no_of_entries += 1

print((total_steps / no_of_entries), "is the average")
