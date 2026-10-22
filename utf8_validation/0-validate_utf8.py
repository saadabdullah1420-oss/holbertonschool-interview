#!/usr/bin/python3
"""Validate UTF-8 byte sequences."""


def validUTF8(data):
    """Return whether the lowest eight bits form valid UTF-8 data."""
    remaining = 0

    for number in data:
        byte = number & 0xFF

        if remaining:
            if byte & 0xC0 != 0x80:
                return False
            remaining -= 1
        elif byte & 0x80 == 0:
            continue
        elif byte & 0xE0 == 0xC0:
            remaining = 1
        elif byte & 0xF0 == 0xE0:
            remaining = 2
        elif byte & 0xF8 == 0xF0:
            remaining = 3
        else:
            return False

    return remaining == 0
