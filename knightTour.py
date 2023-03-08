size = 8
chess_board = [[0 for _ in range(size)] for _ in range(size)]

def print_board():
    for i in range(size):
        for j in range(size):
            print(chess_board[i][j], end= " ")
        print("")

def get_possible_moves(x , y):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possible_moves = []
    for i in range(8):
        next_x = x + pos_x[i]
        next_y = y + pos_y[i]
        if  0 <= next_x < size and  0  <= next_y < size and chess_board[next_x][next_y] == 0:
           possible_moves.append([next_x , next_y])
    return possible_moves

def solve():
    counter = 1
    x = 0
    y = 0
    for i in range(size * size):
        moves = get_possible_moves(x, y)
        min = moves[0]
        for move in moves:
            if len(get_possible_moves(move[0], move[1])) <= len(get_possible_moves(min[0], min[1])):
                min = move
        x = min[0]
        y = min[1]
        chess_board[x][y] = counter
        counter += 1

solve()
print_board()
