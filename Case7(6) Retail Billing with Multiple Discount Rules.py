def generate_invoice(cart_items):
    print("================ INVOICE GENERATOR ================")
    subtotal = 0.0
    total_tax = 0.0

    print(f"{'Item':<12} {'Qty':<5} {'Price':<8} {'Tax Rate':<8} {'Final'}")

    for item in cart_items:
        name, qty, price, category = item
        item_cost = qty * price

        # Calculate Category Tax Rules
        tax_rate = 0.18 if category == "Electronics" else 0.05
        item_tax = item_cost * tax_rate

        subtotal += item_cost
        total_tax += item_tax
        print(f"{name:<12} {qty:<5} ₹{price:<7.2f} {tax_rate * 100:<7.0f}% ₹{item_cost + item_tax:.2f}")

    gross_total = subtotal + total_tax
    discount = 0.0

    # Check conditional thresholds
    if gross_total > 5000:
        discount = gross_total * 0.10  # 10% Flat Threshold Concession
        if discount > 1000:  # Upper capped ceiling rule
            discount = 1000.0

    final_payable = gross_total - discount

    print("-" * 51)
    print(f"Gross Subtotal : ₹{subtotal:.2f}")
    print(f"Collected Tax  : ₹{total_tax:.2f}")
    print(f"Applied Savings: -₹{discount:.2f}")
    print(f"Net Payable    : ₹{final_payable:.2f}")
    print("===================================================\n")


# Database instance payload
shopping_cart = [
    ("Laptop Bag", 1, 1500.0, "Apparel"),
    ("USB Drive", 3, 600.0, "Electronics"),
    ("Wireless Mouse", 1, 2500.0, "Electronics")
]
generate_invoice(shopping_cart)
