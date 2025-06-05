#!/usr/bin/env python3

import unittest
import subprocess
import csv
from pathlib import Path


class TestIslandPerimeterCLI(unittest.TestCase):
    """Acceptance tests for the island perimeter CLI tool."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_data_dir = Path(__file__).parent / "test_data"
        self.test_data_dir.mkdir(exist_ok=True)
        
    def tearDown(self):
        """Clean up after each test method."""
        if self.test_data_dir.exists():
            for file in self.test_data_dir.glob("test_*.csv"):
                file.unlink()
    
    def create_test_csv(self, filename, matrix_data):
        """Helper method to create a CSV file with matrix data."""
        file_path = self.test_data_dir / filename
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in matrix_data:
                writer.writerow(row)
        return file_path
    
    def test_basic_island_perimeter_calculation(self):
        """Test basic island perimeter calculation with example data."""
        test_matrix = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        
        csv_file = self.create_test_csv("test_basic.csv", test_matrix)
        result = self.run_cli_command(csv_file)
        
        self.assertEqual(result.returncode, 0, f"CLI failed with error: {result.stderr}")
        self.assertIn("16", result.stdout, "Expected perimeter of 16 not found in output")

    def run_cli_command(self, csv_file_path):
        """Helper method to run the CLI command and return result."""
        cmd = ["python", "-m", "tool.cli", "-i", str(csv_file_path)]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent  # Run from project root
        )
        return result

if __name__ == "__main__":
    unittest.main()