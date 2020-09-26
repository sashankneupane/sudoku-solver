# <b>M X N Sudoku Solver</b>
Sudoku (数独, sūdoku, digit-single) (/suːˈdoʊkuː/, /-ˈdɒk-/, /sə-/, originally called Number Place) is a logic-based,combinatorial number-placement puzzle. In classic sudoku, the objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

This program, however, is able to solve sudoku problem of any valid grid size with a sub-grid size of M X N. It uses recursion method to solve the puzzle. 

## Program in action
```
puzzle =    [[2,0,0,12,14,0,0,10,0,0,0,9,0,13,1,0],
            [13,15,16,0,0,0,0,0,4,0,0,6,12,0,0,9],
            [0,8,0,6,0,0,0,0,0,7,14,0,0,0,2,11],
            [0,0,1,4,13,8,6,9,0,0,11,0,16,0,0,7],
            [0,1,2,15,0,14,0,0,0,0,0,3,0,0,0,0],
            [3,10,0,8,0,0,0,5,14,16,0,7,2,12,0,1],
            [12,11,0,0,0,0,8,0,0,5,2,0,0,0,4,16],
            [0,9,7,0,0,0,3,2,6,12,13,11,5,0,0,0],
            [1,0,0,0,6,0,5,0,0,14,0,0,0,0,0,0],
            [8,0,0,2,3,0,0,11,0,0,0,0,0,0,13,14],
            [0,6,15,7,10,0,0,14,12,0,0,1,0,0,16,5],
            [0,0,14,10,0,9,15,0,5,0,0,0,3,11,0,2],
            [0,13,0,0,0,0,14,6,0,11,12,0,15,16,0,0],
            [0,0,0,0,11,0,0,16,0,0,10,8,4,1,0,0],
            [0,4,10,3,5,13,12,15,0,1,16,0,0,0,0,0],
            [0,0,0,11,2,4,0,0,3,9,15,0,0,0,12,6]]

order = (4,4)
```
## Solution to the puzzle:
![16X16 sudoku puzzle with 4x4 sub-grid size](images/4by4.png)








