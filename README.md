# python_testing_demo
Demo of unit testing &amp; acceptance testing in Python

## Description of cli program

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