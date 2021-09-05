import sys

Sf: int

k_and_m = sys.stdin.readline()
x = k_and_m.split()
K = int(x[0])
M = int(x[1])


def list_read(l1: str) -> list:
    l1 = l1.split()
    n = int(l1[0])
    l1 = l1[1:]
    for i in range(n):
        l1[i] = int(l1[i])

    return l1


def mod_list(m: int, l: list) -> list:
    """ Changes the list elements by modifying them with the modulus of m
    required"""
    l_copy = l[:]
    for i in range(len(l)):
        l[i] = (l[i] * l[i]) % m

    return l_copy


lists = []
mods = []
for i in range(K):
    l = sys.stdin.readline()
    list1 = list_read(l)
    mod1 = mod_list(M, list1)
    mods.append(mod1)
    lists.append(list1)


sum1 = 0
for x in mods:
    highest = max(x)
    sum1 += highest
    x.remove(highest)

if sum1 < M:
    Sf = sum1

mods_length = len(mods)
# else:
#     # take the second max from one of them
#     for i in range(mods_length):
#         highest = mods[i]
#
#     # we have to make the difference between one of its multiples (M to (M-1)K) largest
#     # find between which it will come



