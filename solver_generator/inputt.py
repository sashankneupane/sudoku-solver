import numpy as np
class inputt:
    def s_input():             #input code for the solver program
        while True:
            try:        #checks invalid input for grid size. rejects string input and more than two inputs
                print("Enter sub-grid size (row and column of small box) of soduku separated by a space. For eg: Grid size of 9 by 9 soduku is 3 3 and of 12 by 12 soduku is 3 4")
                r, c = [int(x) for x in input().split()] #taking raw input of row and column of subgrid
                break
            except:
                print("Invalid entry! Please enter dimension of sub-grid separated by a space."+"\n")
        puzzle = []
        d = r * c
        print("\n"+"Please input numbers by separating with spaces. Use 0 to represent unsolved numbers in the puzzle.")
        for i in range(d):
            while True:
                try:        
                    puzzle.append(list(map(int, input("Row "+ str(i+1)+" :    ").split())))  #checks for string input
                    if len(puzzle[i]) != d:
                        print("Only",d,"numbers, please. No more, no less!")
                        puzzle = puzzle[:-1]
                        continue 
                    elif len([x for x in range(len(puzzle[i])) if puzzle[i][x] > d]) > 0:
                        print("Numbers only upto",d,",please.")
                        puzzle = puzzle[:-1]
                        continue 
                    elif len([x for x in range(len(puzzle[i])) if puzzle[i][x] < 0]) > 0:
                        print("No negative numbers.")  #checks number of inputs, value of input, negative numbers
                        puzzle = puzzle[:-1]
                        continue 
                    break
                except:
                    print("Only numbers! Please try again.")
        order = (r, c)
        while True:     #runs loop until a valid sudoku problem is input
            if inputt.valid(puzzle, order):
                break
            else:
                inputt.s_input()
        return (puzzle, order)

    def valid(array, order):       #checks validity of the input sudoku problem
        d, r, c = order[0]*order[1], order[0], order[1]
        for i in range(d):
            n_zero_col = list(filter(lambda a: a != 0, np.array(array).transpose()[i].tolist()))
            n_zero_row = list(filter(lambda a: a != 0, array[i]))
            if len(n_zero_col) != len(set(n_zero_col)) or len(n_zero_row) != len(set(n_zero_row)):
                print("\n"+"Invalid Sudoku problem. Try again."+"\n")
                return False
        for i in range(0,d,r):
            for j in range(0, d, c):
                box = list(filter(lambda a: a != 0, [array[k][l] for k in range(i, i+r) for l in range(j,j+c)]))    #checks validity of given problem in all boxes
                if len(box) != len(set(box)):
                    print("\n"+"Invalid sudoku problem. Try again."+"\n")
                    return False
        print("\n"+"\n"+"Valid input."+"\n")                
        return True
    
    def g_input():          #input code for the generator program
        print("\n"+"Enter the dimension of sub-size grid of the sudoku you want to generate. Please input values separated by a space."+"\n")
        while True:
            try:        #checks invalid input for grid size. rejects string input and more than two inputs
                print("Enter sub-grid size (row and column of small box) of soduku separated by a space. For eg: Grid size of 9 by 9 soduku is 3 3 and of 12 by 12 soduku is 3 4")
                a, b = [int(x) for x in input().split()] #taking raw input of row and column of subgrid
                break
            except:
                print("Invalid entry! Please enter dimension of sub-grid separated by a space."+"\n")
        return (a,b)