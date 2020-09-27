#WORK UNDER PROGRESSION

from sudoku import sudoku as s
import random

#order = s.generator_input()
#d = order[0]*order[1]

def sudoku_generator(a,b):
    d = a*b
    order = (a,b)
    array = [[0 for x in range(d)] for y in range(d)]
    while True:
        num1, num2 = random.randint(1,d), random.randint(1,d)
        if num1 != num2: break

    array[0][0], array[0][1] = num1, num2
    for i in range(d):
        for j in range(d):
            for k in range(1, d+1):
                if array[i][j] == 0 and s.possible(array, i, j, (a,b), k):
                    array[i][j] = k
    print(s.n_of_sol(array, order))
    return array


s.print_array(sudoku_generator(3,3),(3,3))

            


