def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


num_term = 10
print(f"The first {num_term} of the Fibonacci series are:")
print(list(fibonacci_generator(num_term)))
