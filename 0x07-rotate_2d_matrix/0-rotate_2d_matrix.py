#!/usr/bin/python3
"""
Rotate 2D Matrix 90 degrees clockwise
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise.
    
    Args:
        matrix (list of list of int): A 2D matrix to rotate.
    
    Do not return anything. The matrix must be edited in-place.
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # save topleft  value
            topLeft = matrix[top][left + i]
            # move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # move top left to top right
            matrix[top + i][right] = topLeft
	right -= 1
	left += 1
