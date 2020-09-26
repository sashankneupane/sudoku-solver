import numpy as np


class sudoku:

    def print_array(array, order):   #prints board
        d, r_sb, c_sb = order[0] * order[1], order[0], order[1]
        for x in range(d):
                for y in range(d):
                    if (y + 1) % c_sb == 0 and y+1 != d:
                        print(f"{array[x][y]:3d}", end=" |")
                    else:
                        print(f"{array[x][y]:3d}", end="")
                print()
                if (x + 1) % r_sb == 0 and (x+1) != d:
                    print("-" * ((3 * order[0] * order[1]) + order[0] * 2 ))
        print()

    def possible_values(array, order): 
        r, c, d = order[0], order[1], order[0]*order[1]
        values = []
        for i in range(d):
            for j in range(d):
                if array[i][j] == 0:
                    impossible_values = list(set(array[i]+ np.array(array).transpose()[j].tolist()+[array[k][l] for k in range(i-i%r, i - i%r + r) for l in range(j-j%c,j-j%c+c) if array[k][l]!= 0]))
                    possible_values = [k for k in np.arange(1, d+1) if k not in impossible_values]
                    possible_values.insert(0,(i,j))
                    values.append(possible_values)
        values.sort(key=len)
        return values

    def possible(array, row, col, order,num):        #checks if a value(num) is valid in given position(row, col) in sudoku(array) of dimension(order)
        d, r, c = order[0]*order[1], order[0], order[1]
        for i in range(0,d):        #checks possibility in rows and columns
            if array[row][i] == num or array[i][col] == num:
                return False
        row0, col0= (row//r)*r, (col//c)*c      #this block of code checks possibility in boxes
        for i in range(0, r):         #THIS CAN BE EDITED AND SHORTENED
            for j in range(0, c):
                if array[row0+i][col0+j] == num:
                    return False
        return True

    def solve1(array, order):            #great for harder and bigger problems
        d, r, c = order[0]*order[1], order[0], order[1]
        values = sudoku.possible_values(array, order)
        for i in range(len(values)):
            for value in values:
                for num in range(1, len(value)):
                    row, col = value[0][0], value[0][1]
                    if sudoku.possible(array, row, col, (r, c) ,value[num]):
                        array[row][col] = value[num]
                        sudoku.solve1(array, order)
                        array[row][col] = 0
                return
        sudoku.print_array(array, order)

    def n_of_sol1(array, order):      #great for harder and bigger problems
        solutions = []
        def solve1(array, order):            
            d, r, c = order[0]*order[1], order[0], order[1]
            values = sudoku.possible_values(array, order)
            for i in range(len(values)):
                for value in values:
                    for num in range(1, len(value)):
                        row, col = value[0][0], value[0][1]
                        if sudoku.possible(array, row, col, (r, c) ,value[num]):
                            array[row][col] = value[num]
                            solve1(array, order)
                            array[row][col] = 0
                    return
            solutions.append(array)
        solve1(array,order)
        return len(solutions)

    def solver_input():             #input code for the solver program
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
            if sudoku.valid(puzzle, order):
                break
            else:
                sudoku.solver_input()
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
    
    def generator_input():          #input code for the generator program
        print("\n"+"Enter the dimension of sub-size grid of the sudoku you want to generate. Please input values separated by a space."+"\n")
        while True:
            try:        #checks invalid input for grid size. rejects string input and more than two inputs
                print("Enter sub-grid size (row and column of small box) of soduku separated by a space. For eg: Grid size of 9 by 9 soduku is 3 3 and of 12 by 12 soduku is 3 4")
                a, b = [int(x) for x in input().split()] #taking raw input of row and column of subgrid
                break
            except:
                print("Invalid entry! Please enter dimension of sub-grid separated by a space."+"\n")
        return (a,b)

    def weak_solver(array, order):        #solves puzzles
        r, c, d = order[0], order[1], order[0]*order[1]
        for i in range(d):
            for j in range(d):
                if array[i][j] == 0:
                    impossible_values = list(set(array[i]+ np.array(array).transpose()[j].tolist()+[array[k][l] for k in range(i-i%r, i - i%r + r) for l in range(j-j%c,j-j%c+c) if array[k][l]!= 0]))
                    possible_values = [k for k in np.arange(1, d+1) if k not in impossible_values]
                    if array[i][j] == 0 and len(possible_values) == 1:
                        array[i][j] = possible_values[0]
        try:
            if len([array[i][j] == 0 for i in range(d) for j in range(d) if array[i][j] == 0]) > 0: sudoku.weak_solver(array, order)
        except RecursionError:
            print("This program is too weak. Sorry, it couldn't solve your puzzle.")
        return array