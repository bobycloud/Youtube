# Shopping System - Summing Total Price of Items
item_prices = [12.99, 23.50, 9.99]

# Before
# total = 0
# for price in item_prices:
#     total += price

# After
total = sum(item_prices)

print(f"{total:.2f}")
