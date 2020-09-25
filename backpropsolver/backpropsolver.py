import time

#program input
from program_input import input_
inputt = input_()
puzzle, order = inputt[0], inputt[1]        #order is tuple containing dimension of sudoku, and row and column size of it's subsize

#you can input problems manually here from example_problems.txt... comment out program input block from above and play around!

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

print_array(puzzle, order)
print("\n"+"\n"+"Solving..."+"\n")

def possible(array, row, col, order,num):        #checks if a value(num) is valid in given position(row, col) in sudoku(array) of dimension(order)
    d, r_sb, c_sb = order[0]*order[1], order[0], order[1]
    for i in range(0,d):
        if array[row][i] == num:
            return False
    for i in range(0,d):
        if array[i][col] == num:
            return False
    col0 = (col//c_sb)*c_sb 
    row0 = (row//r_sb)*r_sb
    for i in range(0,r_sb):
        for j in range(0,c_sb):
            if array[row0+i][col0+j] == num:
                return False
    return True

def solve(array, order):            #recursion and backpropagation
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
    print_array(array, order)
    print("\n"+"Solved in ", (time.time() - start_time), " seconds."+"\n")

start_time = time.time()
solve(puzzle, order)