# Non Recursive Approach

def fact1(number):
    i = 1
    for j in range(1, number + 1):
        i *= j
    print(i)

fact1(5)
# 120

## Factorial###


def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

# Both are O(n)
