import math

def is_prime(a: int):
    square_root = math.sqrt(a)
    for i in range(2, round(square_root) + 1):
        if a % i == 0:
            return False
    return True
