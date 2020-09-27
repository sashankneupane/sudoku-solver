import numpy as np

class sudoku:
    solutions = 0

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

    def solve(array, order,print_):        # solves puzzle and returns number of solutions
        def solver(array, order,print_):            #great for harder and bigger problems
            d, r, c = order[0]*order[1], order[0], order[1]
            values = sudoku.possible_values(array, order)
            for i in range(len(values)):
                for value in values:
                    for num in range(1, len(value)):
                        row, col = value[0][0], value[0][1]
                        if sudoku.possible(array, row, col, (r, c) ,value[num]):
                            array[row][col] = value[num]
                            solver(array, order,print_)
                            array[row][col] = 0
                    return
            if print_ == 1: print(np.array(array))
            sudoku.solutions += 1
        solver(array, order, print_)
        return sudoku.solutions