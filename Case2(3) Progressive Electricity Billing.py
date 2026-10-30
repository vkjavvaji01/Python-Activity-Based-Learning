def calculate_electricity_bill(units):
    fixed_charge = 150
    bill_amount = fixed_charge

    # Cascade Slabs
    if units <= 100:
        bill_amount += units * 4.5
    elif units <= 300:
        bill_amount += (100 * 4.5) + (units - 100) * 6.0
    else:
        bill_amount += (100 * 4.5) + (200 * 6.0) + (units - 300) * 8.5

    # Apply Surcharge if bill crosses an threshold
    if bill_amount > 2000:
        bill_amount += bill_amount * 0.05  # 5% Surcharge

    return round(bill_amount, 2)


# Monthly sequence analysis
monthly_consumption = [90, 240, 420, 110]
print("--- Multi-Month Consumption Audit ---")

previous_bill = 0
for month_idx in range(len(monthly_consumption)):
    units = monthly_consumption[month_idx]
    current_bill = calculate_electricity_bill(units)

    alert_flag = ""
    if month_idx > 0 and current_bill > previous_bill * 1.5:
        alert_flag = "⚠️ [UNUSUAL SPIKE DETECTED]"

    print(f"Month {month_idx + 1}: {units} Units -> Cost: ₹{current_bill} {alert_flag}")
    previous_bill = current_bill
