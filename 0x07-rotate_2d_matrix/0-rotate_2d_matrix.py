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
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):  # Start from i+1 to avoid swapping back
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

