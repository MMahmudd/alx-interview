#!/usr/bin/python3
"""
Test_0x07 - Rotate_2D_Matrix
"""
rotate_2d_matrix = __import__('1-rotate_2d_180').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
