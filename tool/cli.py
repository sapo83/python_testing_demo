#!/usr/bin/env python

import argparse
from .main import file_to_matrix, calculate_island_perimeter

# create arparse object
parser = argparse.ArgumentParser(description="Let's find the island perimeter!")

# add arguments
parser.add_argument("-i", "--input_file", dest="filename", required=True, 
                    help="Input file with comma separated matrux values.")        


def main():
    # get arguments
    args = parser.parse_args()
    # read in file
    my_mat = file_to_matrix(args.filename)
    # interpolate missing values
    perimeter = calculate_island_perimeter(my_mat)
    print(perimeter)


if __name__ == "__main__":
    main()