def audit_product_catalogue(catalogue_tuples):
    print("--- Stock Inventory Audit Control ---")
    total_warehouse_valuation = 0.0
    restock_alerts_count = 0

    for item in catalogue_tuples:
        # Tuple Unpacking Layout
        prod_id, label, unit_price, stock_qty = item

        # Validations filter boundaries
        if unit_price < 0 or stock_qty < 0:
            print(f"❌ DATA ERROR ALERT: Malformed entry values for Product ID {prod_id} ({label})")
            continue

        item_asset_value = unit_price * stock_qty
        total_warehouse_valuation += item_asset_value

        if stock_qty <= 5:
            print(f"⚠️ RESTOCK NOTICE   : '{label}' (ID: {prod_id}) is low on stock! [Only {stock_qty} remaining]")
            restock_alerts_count += 1

    print("-" * 50)
    print(f"Aggregate Vault Asset Value: ₹{total_warehouse_valuation:.2f}")
    print(f"Total Priority Reorders Required : {restock_alerts_count} lines.")


# Immutable Database Array Mock
warehouse_catalogue = [
    (101, "Mechanical Keyboard", 4500.0, 12),
    (102, "Ergonomic Wired Mouse", 1200.0, 3),  # Flagged low stock
    (103, "HDMI Monitor Cable", -250.0, 20),  # Malformed validation error
    (104, "USB-C Desktop Dock", 3200.0, 5)  # Flagged low stock
]
audit_product_catalogue(warehouse_catalogue)
