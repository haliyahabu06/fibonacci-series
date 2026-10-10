


def fibonacci_recursive(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

terms = 10

print(f"Fibonacci sequence up to {terms} terms:")
sequence = [fibonacci_recursive(i) for i in range(terms)]
print(sequence)
