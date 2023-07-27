#!/usr/bin/python3
"""
UTF-8 Validation

This module defines a method that determines if a given data set represents a
valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if the given data represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing the bytes of the data.

    Returns:
        bool: True if the data represents a valid UTF-8 encoding, False otherwise.
    """
    bytes_n = 0

    m_one = 1 << 7
    m_two = 1 << 6

    for i in data:

        m_byte = 1 << 7

        if bytes_n == 0:
            # Count the number of bytes in the current UTF-8 character
            while m_byte & i:
                bytes_n += 1
                m_byte = m_byte >> 1

            if bytes_n == 0:
                continue

            if bytes_n == 1 or bytes_n > 4:
                return False

        else:
            # Check if the current byte is part of a UTF-8 character
            if not (i & m_one and not (i & m_two)):
                return False

        bytes_n -= 1

    # Check if all bytes have been consumed
    if bytes_n == 0:
        return True

    return False

