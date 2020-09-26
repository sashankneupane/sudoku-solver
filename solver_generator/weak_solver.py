import time
from sudoku import sudoku as s
puzzle = [[0, 0, 0, 0, 3, 0, 0, 0, 5], [0, 4, 0, 6, 0, 9, 3, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 8],
[7, 9, 0, 0, 0, 1, 6, 0, 3], [0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 3, 0, 9, 4, 6, 7, 0, 0],
[3, 6, 0, 0, 0, 0, 0, 0, 0], [0, 7, 0, 0, 0, 0, 0, 2, 9], [0, 0, 8, 0, 0, 4, 0, 0, 0]]

order = (3,3)

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