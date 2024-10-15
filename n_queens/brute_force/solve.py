from my_iterator import *

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """
    
    def is_safe(combinacion):
        for i in range(0, len(combinacion) - 1):
            for j in range(i + 1, num_queens):
                if combinacion[i] == combinacion[j] or abs(combinacion[i] - combinacion[j]) == j - i:
                    return False
        return True

    solutions_list = []

    # solve it here!
    mi_iterador = My_Iterator(num_queens, num_queens)
    
    for combinacion in mi_iterador.next():
        if is_safe(combinacion):
            solutions_list.append(combinacion)


    return solutions_list 
