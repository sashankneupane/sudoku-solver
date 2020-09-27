import time
from sudoku import sudoku as s
puzzle = [[0, 0, 0, 0, 3, 0, 0, 0, 5], [0, 4, 0, 6, 0, 9, 3, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 8],
[7, 9, 0, 0, 0, 1, 6, 0, 3], [0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 3, 0, 9, 4, 6, 7, 0, 0],
[3, 6, 0, 0, 0, 0, 0, 0, 0], [0, 7, 0, 0, 0, 0, 0, 2, 9], [0, 0, 8, 0, 0, 4, 0, 0, 0]]

order = (3,3)
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
# puzzle, order = s.solver_input()
start_time = time.time()    #stores start time to calculate total run time
s.valid(puzzle, order)      #checks validity of input
num_sol = s.n_of_sol1(puzzle, order)
if num_sol > 1: print("Invalid sudoku problem. It has more than one solution. It's", num_sol,"solutions are: ")    #checks for multiple solutions
print("\n"+"Solving..."+"\n")
solved = s.weak_solver(puzzle, order)
if len([solved[i][j] == 0 for i in range(9) for j in range(9) if solved[i][j] == 0]) > 0:   #checks if the puzzle is solved
    print("Runtime:  ", (time.time()-start_time),"\n")
else:
    s.print_array(solved, order)
    print("\n"+"Solved in ", (time.time() - start_time), " seconds."+"\n")