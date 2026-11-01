n = int(input("Enter n(try 3 or 5) "))
guess = input("How many times does countdown call itself for n = " + str(n) + "? ")

input("recurction - watch each call. Press enter to run")
def countdown(num):
    print(" calls=", n + 1, " your guess", guess, " -> O(n)")


input("Watch calls grow with n. Press Enter")
for size in [3, 5, 10, 100]:
  print(" n =", size, " calls =", size + 1, " -> O(n)")             