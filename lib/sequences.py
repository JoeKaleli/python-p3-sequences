#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    # Generate Fibonacci numbers up to the specified length
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calculate the next Fibonacci number
        fibonacci_sequence.append(next_number)  # Append the next Fibonacci number to the sequence

    print(fibonacci_sequence[:length])  # Print the first 'length' Fibonacci numbers

# Test the function
print_fibonacci(9)
