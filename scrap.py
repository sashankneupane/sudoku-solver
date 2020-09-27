import numpy as np
import time
starttime = time.time()
puzzle = [[2,0,0,12,14,0,0,10,0,0,0,9,0,13,1,0],
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

class solve:

    solutions = 0

    def solver(array, order):            #great for harder and bigger problems
        d, r, c = order[0]*order[1], order[0], order[1]
        values = possible_values(array, order)
        for i in range(len(values)):
            for value in values:
                for num in range(1, len(value)):
                    row, col = value[0][0], value[0][1]
                    if possible(array, row, col, (r, c) ,value[num]):
                        array[row][col] = value[num]
                        solve.solver(array, order, print_)
                        array[row][col] = 0
                return
        print(np.array(array))
        solve.solutions += 1
    
    def solve(array, order, print_):
        solve.solver(array, order, print)_
        return solve.solutions


# def n_of_sol1(array, order):      #great for harder and bigger problems
#     solutions = []
#     def solve1(array, order):            
#         d, r, c = order[0]*order[1], order[0], order[1]
#         values = possible_values(array, order)
#         for i in range(len(values)):
#             for value in values:
#                 for num in range(1, len(value)):
#                     row, col = value[0][0], value[0][1]
#                     if possible(array, row, col, (r, c) ,value[num]):
#                         array[row][col] = value[num]
#                         solve1(array, order)
#                         array[row][col] = 0
#                 return
#         solutions.append(array)
#     solve1(array,order)
#     return len(solutions)

print(solve.solve(puzzle, order))
# print(n_of_sol1(puzzle, order))
print((time.time()-starttime))