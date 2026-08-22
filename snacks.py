snack_name = "Chips"
price = 1.50
quantity = 10
is_available = True

print("Snack:", snack_name)
print("Price:", price)
print("Quantity:", quantity)
print("Available:", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))


total = price * quantity
print("Total Value: $", total)
print("Sale price: $", price - 0.25)
print("Double stock: ", quantity * 2)

print("Is price under $2?", price < 2)
print("More than 5 in stock?", quantity > 5)
print("Is price  exactly $1.50?", price == 1.50)
   