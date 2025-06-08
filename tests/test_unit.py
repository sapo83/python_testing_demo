#!/usr/bin/env python3

import unittest
import numpy as np
from tool.main import calculate_island_perimeter

class TestUnit(unittest.TestCase):

    def test_empty_matrix(self):
        """Test with an empty matrix."""
        matrix = np.array([])
        result = calculate_island_perimeter(matrix)
        self.assertEqual(result, 0)

    def test_single_cell_land(self):
        """Test with a single land cell."""
        matrix = np.array([[1]])
        result = calculate_island_perimeter(matrix)
        self.assertEqual(result, 4, "Single land cell should have perimeter of 4")

    def test_multiple_separate_islands(self):
        """Test with multiple disconnected islands."""
        matrix = np.array([
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ])
        result = calculate_island_perimeter(matrix)
        self.assertEqual(result, 16, "Four separate single cells should have total perimeter of 16")

    def test_edge_island(self):
        """Test with island along matrix edges."""
        matrix = np.array([
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0]
        ])
        result = calculate_island_perimeter(matrix)
        self.assertEqual(result, 8, "Top edge island should have perimeter of 8")