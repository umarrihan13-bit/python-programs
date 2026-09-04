def is_armstrong(number):
    # Convert number to string to easily count digits and access each digit
    num_str = str(number)
    n = len(num_str) # Number of digits

    sum_of_powers = 0
    for digit_char in num_str:
        digit = int(digit_char) # Convert character digit back to an integer
        sum_of_powers += digit ** n # Add the digit raised to the power of n

    return sum_of_powers == number

# --- Let's test it! ---
print(is_armstrong(153)) # Should be True (1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153)
print(is_armstrong(9))   # Should be True (9^1 = 9)
print(is_armstrong(10))  # Should be False (1^2 + 0^2 = 1)
print(is_armstrong(371)) # Should be True (3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371)