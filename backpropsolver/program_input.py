import math
import numpy as np

def input_():
    while True:
        try:        #checks invalid input for grid size. rejects string input and more than two inputs
            print("Enter sub-grid size (row and column of small box) of soduku separated by a space. For eg: Grid size of 9 by 9 soduku is 3 3 and of 12 by 12 soduku is 3 4")
            r_sb, c_sb = r_sb, c_sb = [int(x) for x in input().split()] #taking raw input of row and column of subgrid
            break
        except:
            print("Invalid entry! Please enter dimension of sub-grid separated by a space."+"\n")
    puzzle = []
    d = r_sb*c_sb
    print("\n"+"Please input numbers by separating with spaces. Use 0 to represent unsolved numbers in the puzzle.")
    for i in range(d):
        while True:
            try:        
                puzzle.append(list(map(int, input("Row "+ str(i+1)+" :    ").split())))  #checks for string input
                if len(puzzle[i]) != d:         #limits number of inputs
                    print("Invalid input. Please enter", d, " numbers and represent empty spaces by 0.")
                    puzzle = puzzle[:-1]
                    continue 
                if len([x for x in range(len(puzzle[i])) if puzzle[i][x] > d]) > 0:     #checks validity of input
                    print("Please enter numbers below", d + 1)
                    puzzle = puzzle[:-1]
                    continue
                if len([x for x in range(len(puzzle[i])) if puzzle[i][x] < 0]) > 0:         #checks for negative input
                    print("Negative numbers not accepted. Please enter all numbers again.", d + 1)
                    puzzle = puzzle[:-1]
                    continue
                break
            except:
                print("Invalid Entry. Please try again.")

    order = (r_sb, c_sb)
    while True:     #runs loop until a valid sudoku problem is input
        if check_validity(puzzle, order):
            break
        else:
            input_()
    return (puzzle, order)

def check_validity(array, order):       #checks validity of the sudoku problem
    d, r_sb, c_sb = order[0]*order[1], order[0], order[1]
    for i in range(d):
        n_zero_col = list(filter(lambda a: a != 0, np.array(array).transpose()[i].tolist()))
        n_zero_row = list(filter(lambda a: a != 0, array[i]))
        if len(n_zero_col) != len(set(n_zero_col)) or len(n_zero_row) != len(set(n_zero_row)):
            print("\n"+"Invalid Sudoku problem. Please enter sudoku again."+"\n")
            return False
    for i in range(0,d,r_sb):
        for j in range(0, d, c_sb):
            box = []
            for k in range(i, i+r_sb):
                for l in range(j, j+c_sb):
                    box.append(array[k][l])
            box = list(filter(lambda a: a != 0, box))
            if len(box) != len(set(box)):
                print("\n"+"Invalid sudoku problem. Please enter sudoku again."+"\n")
                return False
    print("\n"+"\n"+"Valid Sudoku problem."+"\n")                
    return True