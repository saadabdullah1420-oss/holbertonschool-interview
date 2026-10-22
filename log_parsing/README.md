# Log Parsing

Read HTTP logs from standard input and calculate cumulative metrics.

Print the total file size and supported status code counts.
Skip malformed entries.
Report every ten input lines, at EOF, and on keyboard interruption.

Usage: ./0-generator.py | ./0-stats.py

Compatible with Python 3.4.3.
