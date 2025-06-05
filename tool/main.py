import numpy as np

def file_to_matrix(file_path):
    """ convert csv file into matrix """

    return np.loadtxt(file_path, dtype=float, delimiter=',')

def calculate_island_perimeter(matrix):
    """ Calculate the perimeter of all land masses in a 2D matrix. """
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    perimeter = 0
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:  # Land cell
                # Check all 4 directions
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    # Edge is exposed if:
                    # 1. Neighbor is out of bounds (matrix boundary)
                    # 2. Neighbor is water (value 0)
                    if (new_row < 0 or new_row >= rows or 
                        new_col < 0 or new_col >= cols or 
                        matrix[new_row][new_col] == 0):
                        perimeter += 1
    
    return perimeter