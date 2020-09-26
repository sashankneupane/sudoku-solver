import numpy as np
puzzle = [[1, 0, 0, 0, 0, 0, 0, 0, 9], [0, 0, 3, 0, 9, 0, 0, 0, 7],[0, 0, 0, 0, 2, 8, 5, 1, 0],
[3, 0, 6, 5, 7, 0, 0, 0, 0], [0, 0, 1, 0, 0, 3, 6, 0, 0], [4, 7, 0, 6, 1, 0, 0, 0, 0],
[0, 6, 0, 0, 3, 0, 0, 0, 0],[0, 0, 0, 8, 0, 0, 0, 5, 0],[7, 0, 0, 0, 0, 5, 1, 0, 2]]

order = (3,3)


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

def solve0(array, order):            #great for smaller problems
    d = order[0]*order[1]
    for row in range(d):  
        for col in range(d):
            if array[row][col] == 0:
                for num in range(1, d+1):
                    if possible(array, row,col,order,num):
                        array[row][col] = num
                        solve0(array, order)
                        array[row][col] = 0
                return 
    print("\n",np.array(array),"\n")

def n_of_sol0(array, order):      #great for smaller problems like 3 by 3 and 3 by 4
    solutions = []
    def solve(array, order):            
        d = order[0]*order[1]
        for row in range(d):  
            for col in range(d):
                if array[row][col] == 0:
                    for num in range(1, d+1):
                        if possible(array, row,col,order,num):
                            array[row][col] = num
                            solve(array, order)
                            array[row][col] = 0
                    return 
        solutions.append(array)
    solve(array,order)
    return len(solutions)
print("\n"+"There is", n_of_sol0(puzzle,order), "solution."+"\n")
solve0(puzzle,order)
