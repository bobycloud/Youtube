def total_price(authenticated: bool, item_price: int, item_quantity: int) -> int | str:
    if authenticated:
        if item_price > 0:
            if item_quantity > 0:
                return item_price * item_quantity
            else:
                return "Quantity must be greater than 0."
        else:
            return "Price must be greater than 0."
    else:
        return "User is not authenticated."


# Usage
item_price = 25
item_quantity = 3
authenticated = True
total = total_price(authenticated, item_price, item_quantity)

print(f"Total price: ${total}") if isinstance(total, int) else print(f"Error: {total}")
