from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    n = int(input())
    fractions = [Fraction(*map(int, input().split())) for _ in range(n)]

    result = product(fractions)
    print(*result)
