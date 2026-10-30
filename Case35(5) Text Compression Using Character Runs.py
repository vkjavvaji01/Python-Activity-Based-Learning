def run_length_compress(input_str):
    if not input_str:
        return ""

    compressed_list = []
    count = 1

    # Iterate through characters tracking repeated runs
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            compressed_list.append(input_str[i - 1] + str(count))
            count = 1

    # Append the last character group
    compressed_list.append(input_str[-1] + str(count))
    compressed_string = "".join(compressed_list)

    print(f"Original Text   : {input_str} (Length: {len(input_str)})")
    print(f"Compressed Text : {compressed_string} (Length: {len(compressed_string)})")

    if len(compressed_string) >= len(input_str):
        print("Decision        : ❌ Compression rejected (No data footprint optimization advantage).\n")
        return input_str
    else:
        print("Decision        :  Compression accepted (Efficient footprint reduction).\n")
        return compressed_string


# Execute evaluation
run_length_compress("WWWWWWWWWWWWBWWWWWWWWWWWWBBB")
run_length_compress("abcdefg")
