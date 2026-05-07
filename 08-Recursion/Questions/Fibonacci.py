## Fibonacci###

def fibonacci(n):
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer.'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

# Iterative Approach
def fibo2(n):
    arr = [0,1]
    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])
    return arr
    
'''
O(2^n) for recursive approach which is horrible and very terrible.
O(n) for iterative approach.
'''