#!/usr/bin/python3
"""Read HTTP logs and print cumulative metrics."""

import re
import sys


def print_stats(total_size, counts):
    """Print file size and sorted status counts."""
    print("File size: {}".format(total_size))
    for code in sorted(counts):
        if counts[code]:
            print("{}: {}".format(code, counts[code]))


def main():
    """Read standard input and calculate log metrics."""
    total_size = 0
    line_count = 0
    counts = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    pattern = re.compile(
        r'^(\d{1,3}(?:\.\d{1,3}){3}) - \[([^\]\r\n]+)\] '
        r'"GET /projects/260 HTTP/1\.1" (\S+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.match(line.rstrip("\r\n"))

            if match:
                ip, date, status, size = match.groups()
                if all(0 <= int(part) <= 255 for part in ip.split(".")):
                    total_size += int(size)
                    if status in counts:
                        counts[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, counts)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
