# Sudoku Solver

A robust Python sudoku solver that handles puzzles of any difficulty with comprehensive validation.

## Features

- ✅ Solves sudoku puzzles of any difficulty (Easy to Very Hard)
- ✅ Validates input grids and detects invalid puzzles
- ✅ Detects unsolvable puzzles and puzzles with multiple solutions
- ✅ Uses constraint propagation and backtracking for efficiency
- ✅ Clean single-function API

## Usage

```python
from sudoku_solver import sudoku

puzzle = [
    [0, 0, 6, 1, 0, 0, 0, 0, 8],
    [0, 8, 0, 0, 9, 0, 0, 3, 0],
    [2, 0, 0, 0, 0, 5, 4, 0, 0],
    [4, 0, 0, 0, 0, 1, 8, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 4, 0],
    [0, 0, 7, 9, 0, 0, 0, 0, 3],
    [0, 0, 8, 4, 0, 0, 0, 0, 6],
    [0, 2, 0, 0, 5, 0, 0, 8, 0],
    [1, 0, 0, 0, 0, 2, 5, 0, 0]
]

try:
    solution = sudoku(puzzle)
    print("Solved!")
    for row in solution:
        print(row)
except ValueError as e:
    print(f"Error: {e}")
