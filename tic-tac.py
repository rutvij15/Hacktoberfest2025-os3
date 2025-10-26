# Tic-Tac-Toe with Unbeatable AI (Minimax Algorithm)

import math

HUMAN = "O"
AI = "X"
EMPTY = " "

board = [EMPTY] * 9

def print_board(b):
    print("\n")
    for i in range(0, 9, 3):
        print(b[i] or " ", "|", b[i+1] or " ", "|", b[i+2] or " ")
        if i < 6:
            print("--+---+--")
    print("\n")

def winner(b):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,1,8),(2,4,6)
    ]
    for a, c, e in wins:
        if b[a] != EMPTY and b[a] == b[c] == b[e]:
            return b[a]
    return None

def moves_left(b):
    return any(spot == EMPTY for spot in b)

def minimax(b, depth, is_max):
    win = winner(b)
    if win == AI: return 1
    if win == HUMAN: return -1
    if not moves_left(b): return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == EMPTY:
                b[i] = AI
                best = max(best, minimax(b, depth+1, False))
                b[i] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == EMPTY:
                b[i] = HUMAN
                best = min(best, minimax(b, depth+1, True))
                b[i] = EMPTY
        return best

def best_move(b):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if b[i] == EMPTY:
            b[i] = AI
            score = minimax(b, 0, False)
            b[i] = EMPTY
            if score > best_val:
                best_val = score
                move = i
    return move

def main():
    print("Tic-Tac-Toe (Human = O, AI = X)")
    print_board(board)

    while True:
        # Human turn
        while True:
            move = int(input("Enter your move (0-8): "))
            if 0 <= move <= 8 and board[move] == EMPTY:
                board[move] = HUMAN
                break
            print("Invalid move, try again.")

        print_board(board)
        if winner(board):
            print("Human wins!")
            break
        if not moves_left(board):
            print("It's a draw!")
            break

        # AI turn
        print("AI is thinking...")
        ai = best_move(board)
        board[ai] = AI
        print_board(board)

        if winner(board):
            print("AI wins!")
            break
        if not moves_left(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
