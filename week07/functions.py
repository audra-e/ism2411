"""
# --- Self-Assessment & Disclosure ---

1. In Exercise 5, I struggled to find the bugs at first, so I asked
Gemini to thoroughly explain the errors. After reviewing the
explanation, I went back to my code and found two of the three bugs.
I then asked ChatGPT to help explain the remaining bug. This taught
me that I need more practice reading error messages and tracing
variables, but I can understand and find bugs when I take my time
and work through the code.

2. apply_discount(price, tier) takes the original price and the
customer's membership tier as inputs. It checks whether the tier
is gold, silver, bronze, or another level and applies the correct
discount. Gold receives 15% off, silver receives 10% off, bronze
receives 5% off, and other tiers receive no discount. It returns
the price after the discount. A colleague could use this function
without reading its body because its name and inputs explain its
purpose.

3. AI Disclosure: I used Gemini and ChatGPT to help explain Python
errors, understand the bugs in my code, and organize parts of this
script. The explanations helped me understand the problems and
identify two of the three bugs myself. AI helped build my
understanding, but I still need to practice debugging so I can
become more independent.
"""


# --- Exercise 1: calculate_tax ---

def calculate_tax(price, rate):
    return price * rate


# Test calls for Exercise 1
print("--- Exercise 1 ---")
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2: apply_discount ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


# Test all four tiers with price = $200
print("\n--- Exercise 2 ---")
print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3: Compose the functions ---

print("\n--- Exercise 3 ---")

# Apply the gold discount to $200
discounted_price = apply_discount(200, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

# Calculate 7% tax on the discounted price
tax_amount = calculate_tax(discounted_price, 0.07)
final_total_demo = discounted_price + tax_amount
print(f"After tax: ${final_total_demo:.2f}")


# Define a function that applies the discount and then calculates tax
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


result = final_price(200, "gold", 0.07)
print(f'final_price(200, "gold", 0.07) = ${result:.2f}')


# --- Exercise 4: Loop + function ---

print("\n--- Exercise 4 ---")

orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5: Debug First, Then Ask ---

print("\n--- Exercise 5 ---")

sales = [120, 80, 250, 175, 90]

# Bug 1 fix:
# The original code replaced the total with each sale.
# Using += adds each sale to the running total.
total = 0

for sale in sales:
    total += sale

print(f"Total: ${total}")


# Bug 2 fix:
# The original for-loop was missing a colon after sales.
# Adding the colon makes the loop syntax valid.
count = 0

for sale in sales:
    count += 1

print(f"Count: {count}")


# Bug 3 fix:
# The original condition used <=, which allowed the index to
# reach len(sales). The last valid index is len(sales) - 1.
# Using < prevents an IndexError.
i = 0

while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6: Scope experiment ---

print("\n--- Exercise 6 ---")

x = 100   # Global variable


def double_it():
    x = 999   # Local variable; different from the global x!
    return x * 2


print(x)           # Prints 100
print(double_it()) # Prints 1998
print(x)           # Prints 100; the global variable has not changed.


# Scope explanation:
# Scope determines where a variable can be accessed in a program.
# A global variable is defined outside a function.
# A local variable is defined inside a function and belongs to that
# function's local scope. Assigning 999 to the local x does not
# change the global x, which remains 100.