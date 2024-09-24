#!/usr/bin/python3
"""
This module contains a function that calculates
the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island represented by 1's in the grid.

    Args:
        grid (list of list of int): A grid where 0 represents water and
        1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Add 4 sides for each land cell
                perimeter += 4

                # If the cell above is land, subtract 2 from the perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # If the cell to the left is land, subtract 2 from the perimeter
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
