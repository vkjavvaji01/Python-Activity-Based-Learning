def simulate_atm(opening_balance, transaction_history):
    print("--- ATM Transaction Sequence Report ---\n")
    balance = opening_balance
    daily_withdrawal_limit = 20000
    total_withdrawn_today = 0

    successful_txns = 0
    rejected_txns = 0

    for txn in transaction_history:
        txn_type, amount = txn  # Tuple unpacking

        if amount <= 0:
            print(f"REJECTED: Invalid amount {amount}")
            rejected_txns += 1
            continue

        if txn_type == "Deposit":
            balance += amount
            successful_txns += 1
            print(f"SUCCESS : Deposited ₹{amount}. Current Balance: ₹{balance}")

        elif txn_type == "Withdrawal":
            if amount > balance:
                print(f"REJECTED: Insufficient Funds for Withdrawal of ₹{amount} (Balance: ₹{balance})")
                rejected_txns += 1
            elif total_withdrawn_today + amount > daily_withdrawal_limit:
                print(f"REJECTED: Exceeded Daily Withdrawal Limit for ₹{amount}")
                rejected_txns += 1
            else:
                balance -= amount
                total_withdrawn_today += amount
                successful_txns += 1
                print(f"SUCCESS : Withdrew ₹{amount}. Current Balance: ₹{balance}")

    print("\n--- Summary ---")
    print(f"Final Balance       : ₹{balance}")
    print(f"Successful Actions  : {successful_txns}")
    print(f"Rejected Actions    : {rejected_txns}")


# Execute Solution
transactions = [("Deposit", 5000), ("Withdrawal", 12000), ("Withdrawal", 10000), ("Deposit", -500),
                ("Withdrawal", 2000)]
simulate_atm(15000, transactions)
