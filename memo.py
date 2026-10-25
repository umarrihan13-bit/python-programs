n = 4

guess = input("predict: how many items in the list? for n = 4? ")
points = list(range(1, n + 1))
print("your guess:", guess, "list:", points, "items:", len(points))


input("predict: what happens to the list size as n grows? Press Enter ")
for size in [4, 10, 100, 1000]:
    print(f"n = {size:<5}, list uses {size:<5} items, in memory")