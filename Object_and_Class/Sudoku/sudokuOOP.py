import random

class Reader:
    @staticmethod
    def get_level():
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
        while level not in {"상", "중", "하"}:
            level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
        if level == '상':
            return 40
        elif level == '중':
            return 34
        else:
            return 28

    @staticmethod
    def get_integer(message, i, j):
        number = input(message)
        while not (number.isdigit() and i <= int(number) <= j):
            number = input(message)
        return int(number)

class SudokuBoard:
    def __init__(self, level):
        self.__goal = SudokuBoard.create_solution_board()
        self.__board = SudokuBoard.copy_board(self.__goal)
        self.__holes = self.make_holes(level)

    @property
    def holes(self):
        return self.__holes

    def make_holes(self, no_of_holes):
        holeset = set()
        while no_of_holes > 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if self.__board[i][j] != 0:
                self.__board[i][j] = 0
                holeset.add((i, j))
                no_of_holes -= 1
        return holeset

    def show_board(self):
        print()
        print('S', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        print('-', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-')
        i = 1
        for row in self.__board:
            print(i, end=' ')
            print('|', end=' ')
            for entry in row:
                if entry == 0:
                    print('.', end=' ')
                else:
                    print(entry, end=' ')
            print()
            i += 1
        print()

    @staticmethod
    def create_board():
        seed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(seed)
        n1 = seed[0]
        n2 = seed[1]
        n3 = seed[2]
        n4 = seed[3]
        n5 = seed[4]
        n6 = seed[5]
        n7 = seed[6]
        n8 = seed[7]
        n9 = seed[8]
        return [[n1, n2, n3, n4, n5, n6, n7, n8, n9],
                [n4, n5, n6, n7, n8, n9, n1, n2, n3],
                [n7, n8, n9, n1, n2, n3, n4, n5, n6],
                [n2, n3, n1, n5, n6, n4, n8, n9, n7],
                [n5, n6, n4, n8, n9, n7, n2, n3, n1],
                [n8, n9, n7, n2, n3, n1, n5, n6, n4],
                [n3, n1, n2, n6, n4, n5, n9, n7, n8],
                [n6, n4, n5, n9, n7, n8, n3, n1, n2],
                [n9, n7, n8, n3, n1, n2, n6, n4, n5]]

    @staticmethod
    def shuffle_ribbons(board):
        top = board[:3]
        middle = board[3:6]
        bottom = board[6:]
        random.shuffle(top)
        random.shuffle(middle)
        random.shuffle(bottom)
        return top + middle + bottom

    @staticmethod
    def transpose(board):
        transposed = []
        for _ in range(len(board)):
            transposed.append([])
        for row in board:
            i = 0
            for entry in row:
                transposed[i].append(entry)
                i += 1
        return transposed

    @staticmethod
    def create_solution_board():
        board = SudokuBoard.create_board()
        board = SudokuBoard.shuffle_ribbons(board)
        board = SudokuBoard.transpose(board)
        board = SudokuBoard.shuffle_ribbons(board)
        board = SudokuBoard.transpose(board)
        return board

    @staticmethod
    def copy_board(board):
        board_clone = []
        for row in board :
            row_clone = row[:]
            board_clone.append(row_clone)
        return board_clone

class SudokuGameController:
    def __init__(self, level):
        self.__sudokuboard = SudokuBoard(level)
        self.__level = level

    def play_sudoku(self):
        self.__sudokuboard.show_board()
        no_of_holes = self.__level
        while no_of_holes > 0:
            i = Reader.get_integer("가로줄번호(1~9): ", 1, 9) - 1
            j = Reader.get_integer("세로줄번호(1~9): ", 1, 9) - 1
            if (i, j) not in self.__sudokuboard.holes:
                print("빈칸이 아닙니다.")
                continue
            n = Reader.get_integer("숫자(1~9): ", 1, 9)
            sol = self.__goal[i][j]
            if n == sol:
                self.__sudokuboard[i][j] = sol
                self.__sudokuboard.show_board()
                self.__sudokuboard.holes.remove((i, j))
                no_of_holes -= 1
            else:
                print(n, "가 아닙니다. 다시 해보세요.")
        print("잘하셨습니다. 또 들려주세요.")

def main():
    level = Reader.get_level()
    SudokuGameController(level).play_sudoku()

if __name__ == "__main__":
    main()
