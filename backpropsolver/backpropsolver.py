import numpy as np
import math 

# #MANUAL INPUT
# d = int(input("Enter the dimension of the sudoku problem:   "))
# if (math.sqrt(dimension) - int(math.sqrt(dimension))) == 0:
#     r_sb = c_sb = int(math.sqrt(dimension))
# else:
#     r_sb, c_sb = [int(x) for x in input("Enter two numbers (dimension of the subsize grid) here (use space to separate):  ").split()]
    
# puzzle = []
# print("Please input numbers by separating with spaces. Use 0 to represent unsolved numbers in the puzzle.")
# for i in range(dimension):
#     puzzle.append(list(map(int, input("Please input numbers of row "+ str(i)+" :    ").split())))


#example problem
order = (12, 3, 4)
puzzle = [[0, 0, 10, 0, 0, 0, 6, 0, 0, 0, 0, 9],
           [0, 4, 0, 6, 2, 0, 0, 11, 0, 0, 0, 10],
           [0, 0, 0, 1, 0, 4, 0, 0, 0, 7, 0, 3],
           [0, 0, 8, 0, 0, 0, 11, 1, 0, 3, 7, 12],
           [1, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 5],
           [0, 12, 0, 0, 5, 2, 0, 7, 4, 6, 0, 0],
           [0, 0, 5, 4, 11, 0, 9, 2, 0, 0, 1, 0],
           [9, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 11],
           [7, 8, 12, 0, 3, 1, 0, 0, 0, 9, 0, 0],
           [8, 0, 11, 0, 0, 0, 3, 0, 5, 0, 0, 0],
           [2, 0, 0, 0, 10, 0, 0, 4, 9, 0, 12, 0],
           [6, 0, 0, 0, 0, 12, 0, 0, 0, 11, 0, 0]]
d, r_sb, c_sb = order[0], order[1], order[2]

def possible(row,col,num):
    global puzzle
    for i in range(0,d):
        if puzzle[row][i] == num:
            return False
    for i in range(0,d):
        if puzzle[i][col] == num:
            return False
    col0 = (col//c_sb)*c_sb
    row0 = (row//r_sb)*r_sb
    for i in range(0,r_sb):
        for j in range(0,c_sb):
            if puzzle[row0+i][col0+j] == num:
                return False
    return True

def solve():
    global puzzle
    for row in range(d):
        for col in range(d):
            if puzzle[row][col] == 0:
                for num in range(1, d+1):
                    if possible(row,col,num):
                        puzzle[row][col] = num
                        solve()
                        puzzle[row][col] = 0
                return 
    print(np.array(puzzle))
    
solve()
