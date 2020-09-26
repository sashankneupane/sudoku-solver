import time
from sudoku import sudoku as s
#to plugin problems, comment out line "s.print_array(puzzle, order)" and uncomment "s.valid(puzzle, order)" and add puzzle and order to the program
#s.valid(puzzle, order)
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
s.valid(puzzle, order)
#puzzle, order = s.solver_input()
s.print_array(puzzle, order)
start_time = time.time()
print("\n"+"Solving..."+"\n")
num_sol = s.n_of_sol1(puzzle, order)
if num_sol > 1:
    print("Invalid sudoku problem. It has", num_sol,"solutions: ")
elif num_sol == 1:
    print("It has only one solution. Calculating..."+"\n")
s.solve1(puzzle, order)
print("\n"+"Solved in ", (time.time() - start_time), " seconds."+"\n")
