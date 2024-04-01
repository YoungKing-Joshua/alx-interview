#!/usr/bin/python3

import sys

def print_stats(total_size, status_counts):
    """Prints the statistics"""
    print(f'Total file size: {total_size}')
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f'{status_code}: {status_counts[status_code]}')

def parse_line(line, total_size, status_counts):
    """Parses a line and updates the metrics"""
    parts = line.split()
    if len(parts) >= 7:
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            if status_code in status_counts:
                total_size += file_size
                status_counts[status_code] += 1
        except ValueError:
            pass
    return total_size, status_counts

def main():
    """Main function"""
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_num = 0

    try:
        for line in sys.stdin:
            line_num += 1
            total_size, status_counts = parse_line(line.strip(), total_size, status_counts)
            if line_num % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()

