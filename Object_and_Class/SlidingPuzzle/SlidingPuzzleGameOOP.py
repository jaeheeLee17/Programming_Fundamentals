import random
import sys
import math

class Reader:
    @staticmethod
    def get_number(size):
        num = input("Type the number you want to move (Type 0 to quit): ")
        while not (num.isdigit() and 0 <= int(num) <= size ** 2 - 1):
            num = input("Type the number you want to move (Type 0 to quit): ")
        return int(num)

class SlidingBoard:
    def __init__(self, size):
        self.__board = SlidingBoard.create_init_board(size)
        self.__empty = self.find_position(0)

    @property
    def board(self):
        return self.__board

    def find_position(self, num):
        for i in range(len(self.__board)):
            for j in range(len(self.__board)):
                if num == self.__board[i][j]:
                    return (i, j)

    def move(self, pos):
        (x, y) = pos
        if self.__empty == (x - 1, y) or self.__empty == (x + 1, y) or \
           self.__empty == (x, y - 1) or self.__empty == (x, y + 1):
           self.__board[self.__empty[0]][self.__empty[1]] = self.__board[x][y]
           self.__board[x][y] = 0
           self.__empty = (x, y)
        else:
            print("Can't move! Try again.")

    def print_board(self):
        i = 0
        for row in self.__board:
            for item in row:
                if item == 0:
                    print("   ", end=' ')
                elif 100 <= item <= 999:
                    print(item, end=' ')
                elif 10 <= item <= 99:
                    print(str(item).rjust(3), end=' ')
                else:
                    print(str(item).rjust(3), end=' ')
            print()
            i += 1

    @staticmethod
    def create_board(numbers):
        board, empty = [], None
        size = int(math.sqrt(len(numbers)))
        for r in range(size):
            k = r * size
            row = numbers[k : k + size]
            if 0 in row:
                c = row.index(0)
                empty = (r, c)
            board.append(numbers[k : k + size])
        return board

    @staticmethod
    def create_init_board(size):
        numbers = [n for n in range(size ** 2)]
        random.shuffle(numbers)
        init_board = SlidingBoard.create_board(numbers)
        return init_board

    @staticmethod
    def create_goal_board(size):
        numbers = [n for n in range(size ** 2)]
        goal_board = SlidingBoard.create_board(numbers)
        return goal_board

class SlidingPuzzleController:
    def __init__(self, size):
        self.__slider = SlidingBoard(size)
        self.__goal = SlidingBoard.create_goal_board(size)
        self.__size = size

    def play(self):
        while True:
            self.__slider.print_board()
            if self.__slider.board == self.__goal:
                print("Congratulations!")
                break
            num = Reader.get_number(self.__size)
            if num == 0:
                break
            pos = self.__slider.find_position(num)
            self.__slider.move(pos)
        print("Please come again.")

def main():
    size = sys.argv[1]
    if size.isdigit() and int(size) > 1:
         SlidingPuzzleController(int(size)).play()
    else:
        print("Not a proper system argument.")

if __name__ == "__main__":
    main()
