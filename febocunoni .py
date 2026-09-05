def generate_fibonacci(num_terms):
    a, b = 0, 1 # Start with the first two Fibonacci numbers

    # List to store the series
    fib_series = []

    # Handle edge cases for 0 or 1 terms
    if num_terms <= 0:
        return fib_series # Returns an empty list
    elif num_terms == 1:
        fib_series.append(a) # Only the first number (0)
        return fib_series

    # Generate the series for more than 1 term
    fib_series.append(a) # Add 0
    fib_series.append(b) # Add 1

    for _ in range(2, num_terms): # Loop from the 3rd term up to num_terms
        next_fib = a + b      # Calculate the next number
        fib_series.append(next_fib) # Add it to our list
        a = b                 # Update 'a' to be the previous 'b'
        b = next_fib          # Update 'b' to be the new 'next_fib'

    return fib_series

# --- Let's test it! ---
# Generate the first 10 Fibonacci numbers
print(generate_fibonacci(10)) # Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generate the first 5 Fibonacci numbers
print(generate_fibonacci(5))  # Expected: [0, 1, 1, 2, 3]