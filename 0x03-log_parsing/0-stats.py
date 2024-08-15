#!/usr/bin/python3

"""
This script reads stdin line by line
and computes metrics.
"""
import sys
import signal

# Initialize variables
total_file_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_statistics():
    """Print the current statistics."""
    print("File size: {}".format(total_file_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))


def signal_handler(sig, frame):
    """Handle the SIGINT signal (CTRL + C) to print statistics and exit."""
    print_statistics()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue
        try:
            ip_address = parts[0]
            date = parts[3] + parts[4]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = int(parts[8])
            file_size = int(parts[9])

            if request != '"GET /projects/260 HTTP/1.1"':
                continue

            total_file_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_statistics()
        except (ValueError, IndexError):
            continue
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

print_statistics()
