#!/usr/bin/python3


def pascal_triangle(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1],[1, 1]]
    else:
        liste = [[1],[1, 1]]
        l = [1, 1]
        for __ in range(3, n+1, 1):
            pass