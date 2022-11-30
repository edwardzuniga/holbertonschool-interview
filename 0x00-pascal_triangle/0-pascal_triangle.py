#!/usr/bin/python3
"""
Pascal's Triangle function
"""


def pascal_triangle(n):
    """
    list of lists of integers representing
    """
    triangle_pascal = []
    for i in range(1, n+1):
        row = []
        for j in range(i):
            if j == 0 or j == i-1:
                n = 1
                row.append(n)
            else:
                n = triangle_pascal[i-2][j-1] + triangle_pascal[i-2][j]
                row.append(n)
        triangle_pascal.append(row)

    return triangle_pascal
