#!/usr/bin/python3
"""
    Pascal Triangle
"""


def pascal_triangle(n):
    """Pascal Triangle"""
    triangle_list = []

    if (n <= 0):
        return triangle_list

    for i in range(n):
        n = 11 ** i
        triangle_list.append(str(n))
    return triangle_list
