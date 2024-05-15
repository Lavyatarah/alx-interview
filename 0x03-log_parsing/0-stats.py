#!/usr/bin/env python3

"""Script to process log data from standard input, calculate metrics, and print statistics."""

import sys
from datetime import datetime

def print_statistics(total_file_size, statuses):
  """Prints the total file size and status code counts."""
  print("File size:", total_file_size)
  for code, count in sorted(statuses.items()):
    if count > 0:
      print(f"{code}: {count}")

total_file_size = 0
statuses = {
  200: 0, 301: 0,
  400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
count = 0  # Track lines processed

try:
  for line in sys.stdin:
    # Validate line format and extract data
    try:
      ip, _, http_method, path, http_version, status_code, file_size = line.split(maxsplit=6)
      status_code = int(status_code)
      file_size = int(file_size)
      if http_method.upper() != "GET" or http_version != "HTTP/1.1" or not status_code in statuses:
        continue  # Skip invalid lines
    except ValueError:
      continue  # Skip lines with non-numeric data

    statuses[status_code] += 1
    total_file_size += file_size
    count += 1

    if count == 10:
      print_statistics(total_file_size, statuses.copy())  # Avoid modifying original dict
      count = 0

except KeyboardInterrupt:
  print_statistics(total_file_size, statuses)

finally:
  print_statistics(total_file_size, statuses)

