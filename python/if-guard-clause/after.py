def total_price(authenticated: bool, item_price: int, item_quantity: int) -> int | str:
    if not authenticated:
        return "User is not authenticated."
    
    if item_price <= 0:
        return "Price must be greater than 0."
    
    if item_quantity <= 0:
        return "Quantity must be greater than 0."
    
    return item_price * item_quantity


# Usage
item_price = 25
item_quantity = 3
authenticated = True
total = total_price(authenticated, item_price, item_quantity)

print(f"Total price: ${total}") if isinstance(total, int) else print(f"Error: {total}")