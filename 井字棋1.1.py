import random

def print_board(board):
    "打印棋盘"
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    "检查玩家是否获胜"
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    "检查是否平局"
    return " " not in "".join("".join(row) for row in board)

def get_move(player):
    "获取玩家的移动"
    while True:
        try:
            row, col = map(int, input(f"玩家 {player}，请选择行和列（例如 '1 1'）: ").split())
            if row not in [1, 2, 3] or col not in [1, 2, 3]:
                raise ValueError
            return row - 1, col - 1
        except ValueError:
            print("输入无效，请用 '行 列' 的格式输入两个数字，范围都是1到3。")

def minimax(board, depth, is_maximizing_player, player, alpha=-float('inf'), beta=float('inf')):
    "Minimax算法的递归函数"
    if check_win(board, "X"):
        return 1 if is_maximizing_player else -1
    if check_win(board, "O"):
        return -1 if is_maximizing_player else 1
    if check_draw(board):
        return 0

    if is_maximizing_player:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    score = minimax(board, depth + 1, not is_maximizing_player, "O" if player == "X" else "X", alpha, beta)
                    board[i][j] = " "  # undo move
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:  # is minimizing player
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    score = minimax(board, depth + 1, not is_maximizing_player, "O" if player == "X" else "X", alpha, beta)
                    board[i][j] = " "  # undo move
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def get_minimax_move(board, player, depth):
    "使用Minimax算法获取AI的移动"
    best_score = float('-inf') if player == "O" else float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                score = minimax(board, depth, player == "O", player)
                board[i][j] = " "  # undo move
                if player == "O" and score > best_score:
                    best_score = score
                    best_move = (i, j)
                if player == "X" and score < best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game_with_minimax():
    "与使用Minimax算法的AI进行井字棋游戏"
    depth = int(input("请输入Minimax算法的搜索深度（1-3）: "))
    if depth < 1 or depth > 3:
        print("无效的搜索深度。")
        return

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    ai_player = "O"
    print("欢迎来到井字棋游戏！")
    print_board(board)

    while True:
        if current_player == "X":
            row, col = get_move(current_player)
        else:
            row, col = get_minimax_move(board, ai_player, depth)

        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)
            if check_win(board, current_player):
                print(f"玩家 {current_player} 赢了！")
                break
            if check_draw(board):
                print("平局！")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("这个位置已经被占用，请重新选择。")
def play_game_with_ai(depth):
    "与AI对战的井字棋游戏"
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    ai_player = "O"
    print("欢迎来到井字棋游戏！")
    print_board(board)

    while True:
        if current_player == "X":
            row, col = get_move(current_player)
        else:
            row, col = get_minimax_move(board, ai_player, depth)

        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)
            if check_win(board, current_player):
                print(f"玩家 {current_player} 赢了！")
                break
            if check_draw(board):
                print("平局！")
                break

            current_player = ai_player if current_player == "X" else "X"
        else:
            print("这个位置已经被占用，请重新选择。")

def play_game_against_human():
    "双人对战模式的井字棋游戏"
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("欢迎来到井字棋游戏 - 双人对战模式！")
    print_board(board)

    while True:
        row, col = get_move(current_player)
        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)
            if check_win(board, current_player):
                print(f"玩家 {current_player} 赢了！")
                break
            if check_draw(board):
                print("平局！")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("这个位置已经被占用，请重新选择。")

def play_game():
    "井字棋游戏的主函数，可以选择对战模式"
    while True:
        game_type = input("请选择游戏类型（双人游戏请输入 '2'，与AI对战请输入 '1'）: ")
        if game_type == '1':
            depth = int(input("请输入Minimax算法的搜索深度（1-3）: "))
            if depth < 1 or depth > 3:
                print("无效的搜索深度。")
                return
            play_game_with_ai(depth)
        elif game_type == '2':
            play_game_against_human()
        else:
            print("无效的游戏类型选择。")
            return

        play_again = input("是否进行下一局游戏？(yes/no): ")
        if play_again.lower() != 'yes':
            print("感谢您的参与，游戏结束！")
            break

if __name__ == "__main__":
    play_game()