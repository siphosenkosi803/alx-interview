#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """

import sys

def print_stats(statistics, total_size):
    """ Prints information """
    print(f"File size: {total_size}")
    for code, count in sorted(statistics.items()):
        if count != 0:
            print(f"{code}: {count}")

# Initialize a dictionary to store the count of each status code
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}

# Initialize counters for total number of lines processed and total file size
line_count = 0
total_size = 0

try:
    # Read each line from the standard input
    for line in sys.stdin:
        # Print statistics after every 10 lines
        if line_count != 0 and line_count % 10 == 0:
            print_stats(status_codes, total_size)

        # Split the line into a list of strings
        line_list = line.split()
        line_count += 1

        try:
            # Extract the file size from the line and add it to the total file size
            total_size += int(line_list[-1])
        except (ValueError, IndexError):
            # If there is an exception (e.g., invalid file size), skip the line
            continue

        try:
            # Extract the status code from the line and increment its count in the dictionary
            status_code = line_list[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, TypeError):
            # If there is an exception (e.g., invalid status code), skip the line
            continue

    # Print the final statistics after processing all lines
    print_stats(status_codes, total_size)

except KeyboardInterrupt:
    # If the user interrupts the script (CTRL + C), print the current statistics
    print_stats(status_codes, total_size)
    raise
