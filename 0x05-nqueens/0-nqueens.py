#!/usr/bin/python3
""" N QUEENS_ALGORITHM_WITH_BACKTRACKING_(RECURSION_INSIDE_LOOP) """
import sys


class NQueen:
    """ Class_for_solving N_Queen_Problem """

    def __init__(self, n):
        """ Global_Variables """
        self.n = n
        self.x = [0 for i in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """ Checks_if_k_Queen_can_be_placed_in_i_column_(True)
        or_if_the_are_attacking_queens_in_row_or_diagonal_(False)
        """

        # j checks_from_1_to_k - 1_(Up_to_previous_queen)
        for j in range(1, k):
            # There_is_already_a_queen_in_column
            # or_a_queen_in_same_diagonal
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def nQueen(self, k):
        """ Tries_to_place_every_queen_in_the_board
        Args:
        k: starting_queen_from_which_to_evaluate_(should_be_1_
        """
        # i_goes_from_column_1_to_column_n_(1st_column_is_1st_index)
        for i in range(1, self.n + 1):
            if self.place(k, i):
                # Queen_can_be_placed_in_i_column
                self.x[k] = i
                if k == self.n:
                    # Placed_all_4_Queens_(A_solution_was_found)
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.res.append(solution)
                else:
                    # Need_to_place_more_Queens
                    self.nQueen(k + 1)
        return self.res


# Main

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
res = queen.nQueen(1)

for i in res:
    print(i)
