import random

BLACK = 'A'
WHITE = 'B'
EMPTY = '--'  

def create_board():
    board = [[EMPTY] * 8 for _ in range(8)]
    board[3][3] = WHITE
    board[4][4] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
    return board

def print_board(board):
    print("  0  1  2  3  4  5  6   7")
    for i, row in enumerate(board):
        print(i, ' '.join(row))

def flip_pieces(board, row, col, color, directions):
    for d in directions:
        r, c = row + d[0], col + d[1]
        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opposite_color(color):
            r += d[0]
            c += d[1]
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == color:
            while True:
                r -= d[0]
                c -= d[1]
                if r == row and c == col:
                    break
                board[r][c] = color

def valid_move(board, row, col, color):
    if board[row][col] != EMPTY:
        return False, []
    
    valid_directions = []
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        r, c = row + d[0], col + d[1]
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opposite_color(color):
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opposite_color(color):
                r += d[0]
                c += d[1]
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == color:
                valid_directions.append(d)
    return len(valid_directions) > 0, valid_directions

def opposite_color(color):
    return BLACK if color == WHITE else WHITE

def get_valid_moves(board, color):
    valid_moves = []
    for r in range(8):
        for c in range(8):
            if valid_move(board, r, c, color)[0]:
                valid_moves.append((r, c))
    return valid_moves

def computer_move(board, color):
    valid_moves = get_valid_moves(board, color)
    if valid_moves:
        move = random.choice(valid_moves)
        make_move(board, move[0], move[1], color)
        print(f"电脑下在了: {move}")

def make_move(board, row, col, color):
    valid, directions = valid_move(board, row, col, color)
    if valid:
        board[row][col] = color
        flip_pieces(board, row, col, color, directions)

def score(board):
    black_count = sum(row.count(BLACK) for row in board)
    white_count = sum(row.count(WHITE) for row in board)
    return black_count, white_count

def play_game():
    board = create_board()
    print("欢迎来到黑白棋游戏！")

    mode = input("请选择对战模式 (1: 双人对战, 2: 人机对战): ")
    if mode == "1":
        player_vs_player = True
    else:
        player_vs_player = False

    max_steps = int(input("请输入在多少步后结算游戏 (推荐40): "))

    turn = BLACK
    steps = 0

    while steps < max_steps:
        print_board(board)
        black_score, white_score = score(board)
        print(f"当前得分: A棋 {black_score} - B棋 {white_score}")
        print(f"当前步数: {steps} / {max_steps}")

        valid_moves = get_valid_moves(board, turn)
        if not valid_moves:
            print(f"{turn} 无法移动，跳过这一轮！")
            turn = opposite_color(turn)
            continue

        if turn == BLACK or player_vs_player:
            move = input(f"轮到{turn} (输入Q退出): ")
            if move.lower() == 'q':
                print("游戏结束，玩家退出。")
                break

            try:
                row, col = map(int, move.split())
                if (row, col) in valid_moves:
                    make_move(board, row, col, turn)
                else:
                    print("无效的移动，请重新输入。")
                    continue
            except (ValueError, IndexError):
                print("请输入合法的坐标。")
                continue
        else:
            computer_move(board, turn)

        steps += 1
        turn = opposite_color(turn)

    print_board(board)
    black_score, white_score = score(board)
    print(f"最终得分: A棋 {black_score} - B棋 {white_score}")
    if black_score > white_score:
        print("A棋胜！")
    elif white_score > black_score:
        print("B棋胜！")
    else:
        print("平局！")

if __name__ == "__main__":
    play_game()