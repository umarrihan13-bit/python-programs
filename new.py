city = input("Enter your city name: ")
temp = float(input("Enter the temperature in C: "))

if temp >35:
    print("Warning: It's extremely hot today")

if temp >25:
        print("great weather outside!")
else:
     print("It's a bit chilly outside.")
if temp >35:
    print("Warning: It's extremely hot today")
elif temp >25:
    print("great weather today!")
elif temp >15:
    print("It's quite cold outside.")
else:
    print("It's a bit chilly outside.")

import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)

print(calendar.calendar(now.year))