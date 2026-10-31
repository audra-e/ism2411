# Reflection 1:

# The most surprising thing about Python lists is how easy they are to change and organize. I did not expect that I could quickly add, remove, sort, and find items using simple commands like append(), remove(), and sort().

#

# Reflection 2:

# One business situation where a Python list could save me time is keeping track of inventory. Instead of manually updating an Excel spreadsheet, I could use a Python list to add new products, remove products that are sold, and organize the inventory automatically.


inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because they cannot be changed.")

print(coords)

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {best}")
print(f"Worst: {worst}")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)
    print(prices)
print(discounted)

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)

    count = len(high_sales)
average = sum(high_sales) / count

print(high_sales)
print(f"Count: {count}")
print(f"Avg: {average:.2f}")
