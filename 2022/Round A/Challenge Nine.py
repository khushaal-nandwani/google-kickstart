# the helper functions have been taken from stack and geekforgeeks
def sum_digits3(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

def closestMultiple(n, x):
    orgnl = n
    if x > n:
        return x
    z = (int)(x / 2)
    n = n + z
    n = n - (n % x)
    if orgnl > n:
        return n + x
    return n


test_case = int(input())


def get_position_to_insert(x: int, N: str) -> int:
    count = 0
    for digit in N:
        if int(digit) > x:
            return count
        count += 1
    return count




for test in range(test_case):
    N_str = input()
    N = int(N_str)
    S = sum_digits3(N)
    close = closestMultiple(S, 9)
    x = close - S
    position = get_position_to_insert(x, N_str)
    print(f"Case #{test + 1}: {N_str[:position]}{str(x)}{N_str[position:]}")


