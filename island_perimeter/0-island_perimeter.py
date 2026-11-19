#!/usr/bin/python3
"""Calculate the perimeter of an island in a rectangular grid."""


def island_perimeter(grid):
    """Return the number of exposed sides of the land cells."""
    perimeter = 0
    for row, cells in enumerate(grid):
        for col, land in enumerate(cells):
            if not land:
                continue
            perimeter += 4
            if row > 0 and grid[row - 1][col]:
                perimeter -= 2
            if col > 0 and cells[col - 1]:
                perimeter -= 2
    return perimeter
