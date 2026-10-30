def generate_monthly_calendar(start_day, days_in_month):
    # Weekday sequence mapping tracker: 0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun
    print("Mon  Tue  Wed  Thu  Fri  Sat  Sun")

    # Generate initial padding block cells
    padding_spaces = "     " * start_day
    print(padding_spaces, end="")

    current_day_column = start_day

    for day in range(1, days_in_month + 1):
        # Format string padding systematically to preserve grids
        print(f"{day:<5}", end="")
        current_day_column += 1

        # Line break shift boundary hit at Sunday column end
        if current_day_column == 7:
            print()  # Carriage return
            current_day_column = 0

    print("\n\n---------------------------------")


# Render Month Profile: Starting Weekday Thursday (3), 31 Days total
print("--- October Calendar Map ---")
generate_monthly_calendar(3, 31)
