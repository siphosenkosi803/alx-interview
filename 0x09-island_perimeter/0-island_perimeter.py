#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """Create a function def island_perimeter(grid):
    that returns the perimeter of the island
    described in grid"""
    outermost = 0
    for k in range(len(grid)):
        for l in range(len(grid[k])):
            if grid[k][l] == 1:
                outermost += 4
                if k > 0 and grid[k-1][l] == 1:
                    outermost -= 2
                if l > 0 and grid[k][l-1] == 1:
                    outermost -= 2
    return outermost
