#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics """
import re
import sys

if __name__ == "__main__":
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    total_size = 0
    counter = 0
    try:
        for line in sys.stdin:
            counter += 1
            data = line.split()
            if len(data) > 2:
                if data[-2] in status_codes:
                    status_codes[data[-2]] += 1
                total_size += int(data[-1])
            if counter == 10:
                print("File size: {}".format(total_size))
                for key, value in sorted(status_codes.items()):
                    if value != 0:
                        print("{}: {}".format(key, value))
                counter = 0
    except Exception:
        pass
    finally:
        print("File size: {}".format(total_size))
        for key, value in sorted(status_codes.items()):
            if value != 0:
                print("{}: {}".format(key, value))
