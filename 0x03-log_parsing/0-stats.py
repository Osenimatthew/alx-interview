#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    """Prints the total file size and the number of lines by status code"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """Parses a log line and returns the status code and file size"""
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None, None


if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)
            if status_code and file_size:
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)
