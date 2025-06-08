# python_testing_demo
Demo of unit testing &amp; acceptance testing in Python

## Description of app

A command-line tool that accepts a two-dimensional grid representing a map where 1s represent land and 0s represent water, and produces the total perimeter of all land masses. The perimeter is calculated by counting each land cell's exposed edges (edges that border water or the grid boundary).

## Example
```
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
```

## Execution

```
python_testing_demo % python -m tool.cli -i ./example_data/example_1.csv
```

## Testing execution

```
python -m unittest tests.test_acceptance -v
python -m unittest tests.test_unit -v
```