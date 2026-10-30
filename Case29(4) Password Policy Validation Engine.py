def validate_password(password):
    failures = []

    # Rule 1: Length check
    if len(password) < 8:
        failures.append("Must be at least 8 characters long.")

    # Rule 2 & 3: Category validation loops
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True

    if not has_upper: failures.append("Missing an uppercase letter (A-Z).")
    if not has_lower: failures.append("Missing a lowercase letter (a-z).")
    if not has_digit: failures.append("Missing a numeric digit (0-9).")

    # Rule 4: Prohibited substring check
    if "123" in password or "password" in password.lower():
        failures.append("Contains a prohibited weak pattern ('123' or 'password').")

    # Output decision matrix
    print(f"Evaluating: '{password}'")
    if len(failures) == 0:
        print("Verdict: ✅ STRONG PASSWORD\n")
    else:
        print("Verdict: ❌ WEAK PASSWORD")
        for fail in failures:
            print(f" -> Failed Rule: {fail}")
        print()


# Test Suite Engine
validate_password("weak")
validate_password("SecurePass123!")
validate_password("ValidP@ss2026")
