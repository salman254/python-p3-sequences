#!/usr/bin/env python3

def print_fibonacci(n):
    if n <= 0:
        print([])
        return
    
    if n == 1:
        print([0])
        return
    
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to length n
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    print(fib_sequence)
