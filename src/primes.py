import math

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for n in range(2, math.isqrt(num) + 1):
        if num % n == 0:
            return False
    return True
