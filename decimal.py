binary_str = "1101"
decimal_num = int(binary_str, 2)

print(decimal_num)

binary_str = "1101"
decimal_num = 0
power = 0

for bit in reversed(binary_str):
    if bit == '1':
      decimal_num += 2 ** power
    power += 1
    
print(decimal_num)