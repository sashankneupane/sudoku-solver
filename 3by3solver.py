import numpy as np
import math 
dimension = int(input("Enter the dimension of the sudoku you want to solve:  "))
m = int(math.sqrt(dimension))
#code to input the sudoku problem 
print("\n" + "You will be prompted to enter numbers of the sudoku row wise. For empty squares, please enter 0 and enter all numbers without any spaces." + "\n")
print("For example:")
print("004050009"+"\n"+"\n")
sudoku = []
for i in range(9):
    print("Input the numbers of row " + str(i+1) + ".")
    sudoku.append(list(map(int, input().replace("", " ")[1:-1].split())))

#finds possible values for a placeholder and replaces it with the value if the number of possible values is only one
def sudoku_solver(array):
    for i in range(dimension):
        for j in range(dimension):
            if array[i][j] == 0:
                impossible_values = list(set(array[i]+np.array(array).transpose()[j].tolist()+box_range(array, i, j)))
                possible_values = [k for k in [1,2,3,4,5,6,7,8,9] if k not in impossible_values]
                if array[i][j] == 0 and len(possible_values) == 1:
                    array[i][j] = possible_values[0]
    return array

#returns possible values for a placeholder from boxes
def box_range(array, i, j):
    impossible_values = []
    for i in range(i - i%m, i - i%m + m):
        for j in range(j - j%m, j - j%m + m):
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
while not completion_check(sudoku):
    sudoku = sudoku_solver(sudoku)

#prints the calculated solution
print("The solved sudoku is:")
print(np.array(sudoku))
