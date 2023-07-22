#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """

import sys

def printsts(dic, size):
    """ Prints information """
    # Print the total file size
    print("File size: {:d}".format(size))

    # Print the count of each status code in ascending order
    for code, count in sorted(dic.items()):
        if count != 0:
            print(f"{code}: {count}")

# Initialize a dictionary to store the count of each status code
sts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

# Initialize counters for total number of lines processed and total file size
count = 0
size = 0

try:
    # Read each line from the standard input
    for line in sys.stdin:
        # Print statistics after every 10 lines
        if count != 0 and count % 10 == 0:
            printsts(sts, size)

        # Split the line into a list of strings
        stlist = line.split()
        count += 1

        try:
            # Extract the file size from the line and add it to the total file size
            size += int(stlist[-1])
        except:
            # If there is an exception (e.g., invalid file size), skip the line
            pass

        try:
            # Extract the status code from the line and increment its count in the dictionary
            if stlist[-2] in sts:
                sts[stlist[-2]] += 1
        except:
            # If there is an exception (e.g., invalid status code), skip the line
            pass

    # Print the final statistics after processing all lines
    printsts(sts, size)

except KeyboardInterrupt:
    # If the user interrupts the script (CTRL + C), print the current statistics
    printsts(sts, size)
    raise

