def generate_numeric_diamond(n):
    if n <= 0 or n % 2 == 0:
        print("Please enter a positive odd integer.")
        return

    print(f"--- Symmetric Hollow Diamond Pattern (Size: {n}) ---\n")

    # Upper half of diamond
    spaces = n // 2
    for i in range(1, n + 1, 2):
        row_str = " " * spaces
        if i == 1:
            row_str += str(1)
        else:
            row_str += str(i) + " " * (2 * (i - 2) + 1) + str(i)
        print(row_str)
        spaces -= 1

    # Lower half of diamond
    spaces = 1
    for i in range(n - 2, 0, -2):
        row_str = " " * spaces
        if i == 1:
            row_str += str(1)
        else:
            row_str += str(i) + " " * (2 * (i - 2) + 1) + str(i)
        print(row_str)
        spaces += 1


# Execute Solution
generate_numeric_diamond(7)
