# This is to build a solver for any valid sudoku quiz
# This should be setup as a OOP method.

# question from https://www.websudoku.com/
# It also allows to verify answer



### In this version, it is capable of solving raw material in either str form or int form.
class Sudoku(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """
    STR_LIST = ["1", "2", "3", "4", "5","6", "7", "8", "9"]
    INT_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    def __init__(self, puzzle):
        """
        An empty checkerboard -
        the structure should be a nested list of 10 lists where each list contain 10 spot, default to filled with 0

        When initiated:
        The empty checkerboard is skipped by directly loading a pre-written board with numbers on.
        The pre-written board follows the same structure as a nested list like empty.

        puzzle should be a 2D list that contains constently <str> or <int>

        blank is whatever the empty spot is, it can be 0, " ", or "0", or " ".
        We must input raw data with same format:
            if blank is <str>, then the data is <str>, output will be "1" to "9"
            if blank is <int>, then the data is <int>, output will be 1 to 9
        """
        type_check = type(puzzle[0][0])
        print('Type: ', type_check)
        blank = None
        for row in puzzle:
            for element in row:
                assert type(element) == type_check
                if element not in Sudoku.STR_LIST and element not in Sudoku.INT_LIST:
                    blank = element

        self.board = puzzle
        self.blank = blank
        print("?????????????????????????????????", self.blank)
        self.valid = Sudoku.STR_LIST if type_check == str else Sudoku.INT_LIST
        self.puzzle_type = type_check

        print(self.puzzle_type, ' puzzle is generated:')
        print(self)
        print('')

        # Also create a permanent puzzle copy for future use
        self.puzzle = self.board_mem()

    def __str__(self):
        """to just print the current checker board
        also add a coordinate axis for easier read
        """

        def process_raw(row):
            x = '|'
            for i in row:
                if i == self.blank:
                    x += '.'
                else:
                    x += str(i)
                x += "  "

            return x[0:9] + '  ' + x[9:18] + '  ' + x[18:]


        to_print = ''
        y_num = 9
        separ = '    -----------------------------'
        x_num = '    1  2  3    4  5  6    7  8  9'

        for i in self.board:
            str_row = process_raw(i)
            to_print += str(y_num) + '  ' + str_row + '\n'
            if y_num in [7, 4]:
                to_print += '\n'
            y_num -= 1

        to_print += separ + '\n' + x_num
        return to_print


    # Build up class attributes to for future to check up the rows, columns and grids.
    def row(self, n):
        """output a row of numbers
        n: int 1-9
        return: a list of numbers extracted from the row
        """
        rows = self.board[:] # make a copy
        return rows[9-n]

    def col(self, n):
        """output a column of numbers
        n: int 1-9
        return: a list of numbers extracted from the column
        """
        columns = [[self.board[i][j] for i in range(9)] for j in range(9)]
        return columns[n-1]

    def grid(self, n):
        """output a grid of 3*3 in the checkboard
        n: int 1-9

        The grid index on the checkerboad will be:
        1 2 3
        4 5 6
        7 8 9

        return: a list of numbers extracted from the grid
        """
        g1 = sum([[self.board[i][j] for j in range(0, 3)] for i in range(0, 3)], [])
        g2 = sum([[self.board[i][j] for j in range(3, 6)] for i in range(0, 3)], [])
        g3 = sum([[self.board[i][j] for j in range(6, 9)] for i in range(0, 3)], [])
        g4 = sum([[self.board[i][j] for j in range(0, 3)] for i in range(3, 6)], [])
        g5 = sum([[self.board[i][j] for j in range(3, 6)] for i in range(3, 6)], [])
        g6 = sum([[self.board[i][j] for j in range(6, 9)] for i in range(3, 6)], [])
        g7 = sum([[self.board[i][j] for j in range(0, 3)] for i in range(6, 9)], [])
        g8 = sum([[self.board[i][j] for j in range(3, 6)] for i in range(6, 9)], [])
        g9 = sum([[self.board[i][j] for j in range(6, 9)] for i in range(6, 9)], [])
        grids = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
        return grids[n-1]

    # Define moves to add numbers to the board
    def insert(self, x, y, value):
        """to insert a value into the checkerboard
        for convenience, indext start from 1, and act like coordinates
        """
        self.board[9-y][x-1] = value

    def board_mem(self):
        """a snpashot of current board
        for future roll back
        """
        return [self.board[i][:] for i in range(9)]


    # define some verification method
    def get_value(self, coor):
        """return the number at a coordinate in the checkerboard
        coor: a tuple with two value (x, y)
        return: the number on the checkerboard
        """
        return self.board[9-coor[1]][coor[0]-1]

    def get_row_col_sub(self, coor):
        """return a list of 3 list, that contains the related row, column and sub grid of that coor
        """
        row_at = self.row(coor[1])
        col_at = self.col(coor[0])

        if coor[0] in [1,2,3]:
            if coor[1] in [1,2,3]:
                n = 7
            elif coor[1] in [4,5,6]:
                n = 4
            elif coor[1] in [7,8,9]:
                n = 1

        elif coor[0] in [4,5,6]:
            if coor[1] in [1,2,3]:
                n = 8
            elif coor[1] in [4,5,6]:
                n = 5
            elif coor[1] in [7,8,9]:
                n = 2

        elif coor[0] in [7,8,9]:
            if coor[1] in [1,2,3]:
                n = 9
            elif coor[1] in [4,5,6]:
                n = 6
            elif coor[1] in [7,8,9]:
                n = 3

        grid_at = self.grid(n)
        return [row_at, col_at, grid_at]

    def no_conflict(self):
        """return if there is a conflict in the board, where 2 same number (!=self.blank) showed up:
        in the same row, column or grid

        return True if no conflicts were found
        return False if conflicts were found
        """
        all_subs = [self.row(n) for n in range(1,10)] + [self.row(n) for n in range(1,10)] + [self.grid(n) for n in range(1,10)]
        for sub in all_subs:
            check_list = []
            for i in sub:
                if i != self.blank:
                    if i not in check_list:
                        check_list.append(i)
                    else:
                        return False
        return True

    def all_filled(self):
        """To ensure all the place is filled with a number"""
        return all(all(j != self.blank for j in i) for i in self.board)


    def valid_solution(self):
        """To check if the puzzle is solved"""
        return self.all_filled() and self.no_conflict()


    def analysis(self):
        """return a dict of every vacant coordinate linked to the possible value it can be put in
        the result dict should be in the form of :
        {(x,y): [v1, v2, v3], (x,y): [v1, v2, v3], (x,y): [v1, v2, v3]}
        """
        result = {}
        for x in range(1,10):
            for y in range(1,10):
                coordinate = (x, y)
                if self.get_value(coordinate) == self.blank:
                    all_subs = self.get_row_col_sub(coordinate)
                    cant_be = [i for i in sum(all_subs, []) if i != self.blank]
                    all_nums = self.valid
                    can_be = [i for i in all_nums if i not in cant_be]
                    result[coordinate] = can_be
        return result

    def direct_deduce(self):
        """To analyze each vacant coordinate, and if there is only one possible value for it
        fill it in with the value on the checkerboard"""

        def deduce():
            to_be_deduced = []
            all_possible = self.analysis()
            for key, value in all_possible.items():
                if len(value) == 1:
                    to_be_deduced.append((key, value[0]))
            return to_be_deduced

        to_be_filled = deduce()
        while to_be_filled:
            for coor, value in to_be_filled:
                self.insert(coor[0], coor[1], value)
            to_be_filled = deduce()

    def feasible(self):
        """return True if all vacant spot can still fill in a possible number"""
        all_possible = self.analysis()
        for key, value in all_possible.items():
            if len(value) == 0:
                return False
        if self.all_filled():
            return False
        return True

    def hypothesize(self):
        """analyze the board and picke the coordinate with least possible values
        then generate a list of sublist which contains coor and a possible value
        in the form of:
        [[(x,y), value],[(x,y), value],[(x,y), value]]
        """
        result = []
        all_possible = self.analysis()
        coor = min(all_possible, key=lambda x: len(all_possible.get(x)))
        value = all_possible[coor]
        for i in value:
            result.append([coor, i])
        return result

    def hyper_move(self, to_move):
        """try to move a hypothsized spot with a possible number
        to_move: a list as a pair of coordinates and possible values in the form of:
        [(x,y), value]
        according to to_move, the board insert this hyperthetical value
        """
        self.insert(to_move[0][0], to_move[0][1], to_move[1])

    # Final solution
    def solve(self):
        """This will solve the problem and fill the self.board with correct answer
        it will then print(self) to show the answer
        """
        snapshot_board = []
        snapshot_to_do = []
        count = 0
        hypo_layer = 0
        hypo_layer_all = []

        while not self.valid_solution():
            count += 1
            hypo_layer_all.append(hypo_layer)
            self.direct_deduce()

            if self.valid_solution():
                break

            if self.feasible():
                attemp_move = self.hypothesize()
                for i in range(len(attemp_move)-1):
                    snapshot_board.append(self.board_mem())
                snapshot_to_do += attemp_move
                self.hyper_move(snapshot_to_do.pop())
                hypo_layer += 1

            else:
                hypo_layer -= 1
                self.board = snapshot_board.pop()
                self.hyper_move(snapshot_to_do.pop())


        print('problem solved!')
        print(self)
        print('Total hypothesis: ', count)
        print('max_layer_counted:', max(hypo_layer_all))
        print('\n')


if __name__ == '__main__':
    # list out 4 problems for test case

    # websudoku easy puzzle 10
    easy_data_10 = [
        [0,1,0,0,6,0,0,9,0],
        [9,0,5,1,0,0,0,0,0],
        [0,4,8,7,0,9,6,0,0],
        [0,7,6,0,8,0,1,5,0],
        [8,0,0,0,0,0,0,0,7],
        [0,5,3,0,4,0,2,6,0],
        [0,0,4,8,0,5,9,2,0],
        [0,0,0,0,0,4,7,0,5],
        [0,9,0,0,3,0,0,8,0],
    ]

    # websudoku medium puzzle 10
    medium_data_10 = [
        [5,0,2,1,8,0,0,0,0],
        [9,1,0,0,5,0,2,0,0],
        [0,4,6,0,0,2,0,0,1],
        [0,0,0,2,0,1,0,0,8],
        [0,0,1,0,0,0,4,0,0],
        [4,0,0,3,0,9,0,0,0],
        [1,0,0,7,0,0,8,5,0],
        [0,0,9,0,1,0,0,7,4],
        [0,0,0,0,2,8,9,0,6],
    ]

     # websudoku hard puzzle 10
    hard_data_10 = [
        [0,0,0,3,7,0,0,0,5],
        [8,0,0,0,5,1,3,0,0],
        [0,5,0,0,0,0,0,6,2],
        [9,4,0,0,0,0,0,0,0],
        [0,0,0,7,0,8,0,0,0],
        [0,0,0,0,0,0,0,5,4],
        [1,6,0,0,0,0,0,4,0],
        [0,0,3,1,2,0,0,0,7],
        [5,0,0,0,6,4,0,0,0],
    ]

    # websudoku evil puzzle 1
    evil_data_1 = [
        [0,0,1,8,3,0,0,0,0],
        [9,6,5,0,0,0,0,0,0],
        [0,0,0,0,1,0,9,0,0],
        [4,0,0,0,0,0,0,1,0],
        [0,0,9,6,0,4,3,0,0],
        [0,8,0,0,0,0,0,0,2],
        [0,0,7,0,9,0,0,0,0],
        [0,0,0,0,0,0,5,4,8],
        [0,0,0,0,2,5,1,0,0],
    ]

     # websudoku evil puzzle 10
    evil_data_10 = [
        [0,0,0,0,5,0,0,9,0],
        [0,5,0,6,8,0,0,0,0],
        [9,3,7,0,0,0,0,0,0],
        [2,0,0,0,0,0,5,0,0],
        [0,9,0,7,0,2,0,8,0],
        [0,0,6,0,0,0,0,0,4],
        [0,0,0,0,0,0,2,3,6],
        [0,0,0,0,4,3,0,5,0],
        [0,1,0,0,9,0,0,0,0],
    ]


    # easy10 = Sudoku(easy_data_10)
    # easy10.solve()

    medium10 = Sudoku(medium_data_10)
    # medium10.solve()

    # hard10 = Sudoku(hard_data_10)
    # hard10.solve()
    #
    # evil1 = Sudoku(evil_data_1)
    # evil1.solve()
    #
    # evil10 = Sudoku(evil_data_10)
    # evil10.solve()


    # Addtional test case: Hardest SUDOKU ever!
    # ultimate_puzzle = [
    #     [8,0,0,0,0,0,0,0,0],
    #     [0,0,3,6,0,0,0,0,0],
    #     [0,7,0,0,9,0,2,0,0],
    #     [0,5,0,0,0,7,0,0,0],
    #     [0,0,0,0,4,5,7,0,0],
    #     [0,0,0,1,0,0,0,3,0],
    #     [0,0,1,0,0,0,0,6,8],
    #     [0,0,8,5,0,0,0,1,0],
    #     [0,9,0,0,0,0,4,0,0],
    # ]
    #
    # import time
    # ultimate_sudoku = Sudoku(ultimate_puzzle)
    # start_time = time.time()
    # ultimate_sudoku.solve()
    # print(f"--- {time.time() - start_time}s seconds ---\n")
