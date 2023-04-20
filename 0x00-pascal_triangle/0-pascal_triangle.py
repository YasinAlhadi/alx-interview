#!/usr/bin/python3
"""
    Pascal Triangle
"""


def pascal_triangle(n):
    """Pascal Triangle"""
    if (n <= 0):
        return []
    for i in range(n):
        print(' '*(n-i), end='')
        print(' '.join(map(str, str(11**i))))
