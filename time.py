n = 4

guess = input("Total points :1+2+3+4 = ")

input("Formula: one calculation. Press Enter to continue...")
total = n * (n + 1)
print("Total =", total," steps = 1")

input("loop: adds one student at a time. Press Enter to continue...")
total = 0
for student in range(1, n + 1):
    total += student
print("Total=", total, "steps =", n)

input("Double Loop: counts every single point. Press Enter to continue...")
total = 0
steps = 0
for student in range(1, n + 1):
    for point in range(1, student + 1):
        total += 1
        steps += 1
print("Total=", total, "steps =", steps)        