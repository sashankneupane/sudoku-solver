import numpy as np 
import math 

dimension = int(input("Enter the dimension of the sudoku problem:   "))
if (math.sqrt(dimension) - int(math.sqrt(dimension))) == 0:
    m = n = int(math.sqrt(dimension))
else:
    m, n = [int(x) for x in input("Enter two numbers (dimension of the subsize grid) here (use space to separate):  ").split()]
    

#inputting the puzzle
puzzle = np.full((dimension, dimension), 0, dtype = object)
print(puzzle)
print("Please input numbers by separating with spaces. Use 0 to represent unsolved numbers in the puzzle.")
for i in range(dimension):
    puzzle[i] =  list(map(int, input("Please input numbers of row "+ str(i)+" :    ").split()))
puzzle = puzzle.tolist()

#finds possible values for a placeholder and replaces it with the value if the number of possible values is only one
def puzzle_solver(array):
    for i in range(dimension):
        for j in range(dimension):
            if array[i][j] == 0:
                impossible_values = list(set(array[i]+np.array(array).transpose()[j].tolist()+box_range(array, i, j)))
                possible_values = [k for k in np.arange(1, dimension+1) if k not in impossible_values]
                if array[i][j] == 0 and len(possible_values) == 1:
                    array[i][j] = possible_values[0]
    return array

#returns possible values for a placeholder from boxes
def box_range(array, i, j):
    impossible_values = []
    for i in range(i - i%m, i - i%m + m ):
        for j in range(j - j%n, j - j%n + n):
            if array[i][j] != 0:
                impossible_values.append(array[i][j])
    return impossible_values

#checks if the solution is already completed
def completion_check(array):
    for i in range(dimension):
        for j in range(dimension):
            if array[i][j] == 0:
                return False
    return True


#main loop to keep iterating until complete solution is found
while not completion_check(puzzle):
    puzzle = puzzle_solver(puzzle)

#prints the calculated solution
print("The solved sudoku problem is:")
print(np.array(puzzle))



