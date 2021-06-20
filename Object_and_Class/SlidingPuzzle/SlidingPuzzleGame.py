import random
import sys

def create_init_board(size):
    numbers = [n for n in range(size ** 2)]
    random.shuffle(numbers)
    board, empty = [], None
    for r in range(size):
        k = r * size
        row = numbers[k : k + size]
        if 0 in row:
            c = row.index(0)
            empty = (r, c)
        board.append(numbers[k : k + size])
    return board

def create_goal_board(size):
    numbers = [n for n in range(size ** 2)]
    board, empty = [], None
    for r in range(size):
        k = r * size
        row = numbers[k : k + size]
        if 0 in row:
            c = row.index(0)
            empty = (r, c)
        board.append(numbers[k : k + size])
    return board

def print_board(board):
    i = 0
    for row in board:
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

def get_number(size):
    num = input("Type the number you want to move (Type 0 to quit): ")
    while not (num.isdigit() and 0 <= int(num) <= size ** 2 - 1):
        num = input("Type the number you want to move (Type 0 to quit): ")
    return int(num)

def find_position(num, board):
    for i in range(len(board)):
        for j in range(len(board)):
            if num == board[i][j]:
                return (i, j)

def move(pos, empty, board):
    (x, y) = pos
    if empty == (x - 1, y) or empty == (x + 1, y) or \
       empty == (x, y - 1) or empty == (x, y + 1):
       board[empty[0]][empty[1]] = board[x][y]
       board[x][y] = 0
       return (pos, board)
    else:
       print("Can't move! Try again.")
       return (empty, board)

def sliding_puzzle(size):
    board = create_init_board(size)
    goal = create_goal_board(size)
    empty = find_position(0, board)
    while True:
        print_board(board)
        if board == goal:
            print("Congratulations!")
            break
        num = get_number(size)
        if num == 0:
            break
        pos = find_position(num, board)
        (empty, board) = move(pos, empty, board)
    print("Please come again.")

def main():
    size = sys.argv[1]
    if size.isdigit() and int(size) > 1:
         sliding_puzzle(int(size))
    else:
        print("Not a proper system argument.")

if __name__ == "__main__":
    main()
