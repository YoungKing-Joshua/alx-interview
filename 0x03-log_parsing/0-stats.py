#!/usr/bin/python3
"""Log Parsing"""
import sys

if __name__ == '__main__':
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """Print log and reset counters"""
        print('File size: {}'.format(file_size))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print('{}: {}'.format(key, status_codes[key]))
        # Reset counters after printing
        file_size = 0
        for key in status_codes:
            status_codes[key] = 0

    def parse_line(line):
        """Checks for matches"""
        try:
            line = line.strip()  # Strip newline character
            words = line.split(' ')
            # File size is last parameter on stdout
            file_size += int(words[-1])
            # Status code comes before file size
            status_code = int(words[-2])
            # Check if status code is valid
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (ValueError, IndexError):
            pass

    line_num = 0  # Start line count from 0
    try:
        for line in sys.stdin:
            parse_line(line)
            line_num += 1
            if line_num % 10 == 0:
                print_stats()
        # Print final statistics
        print_stats()
    except KeyboardInterrupt:
        # Handle keyboard interruption gracefully
        print_stats()
        raise

