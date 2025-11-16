# TASK 2: TIC-TAC-TOE AI using Minimax

PLAYER = 'X'
AI = 'O'

# 1. Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# 2. Function to check for a winner
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player: return True
    return False

# 3. Function to check if the board is full (Draw)
def is_board_full(board):
    for row in board:
        if ' ' in row: return False
    return True

# 4. The Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, AI): return 10 - depth
    if check_winner(board, PLAYER): return depth - 10
    if is_board_full(board): return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

# 5. Function to find the AI's best move
def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = ' '
                
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# 6. Main Game Loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = PLAYER 
    
    print("--- Tic-Tac-Toe Game (You are X) ---")
    print_board(board)
    
    while True:
        if current_player == PLAYER:
            try:
                # User Input
                row = int(input("Enter row (0, 1, 2) for X: "))
                col = int(input("Enter col (0, 1, 2) for X: "))
                
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    board[row][col] = PLAYER
                    current_player = AI
                else:
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Use numbers 0, 1, 2.")
                continue

        else: # AI's turn
            print("AI (O) is thinking...")
            move = find_best_move(board)
            if move:
                board[move[0]][move[1]] = AI
                current_player = PLAYER
            
        print_board(board)

        # Check Game Status
        if check_winner(board, PLAYER):
            print("You Win! (X)")
            break
        elif check_winner(board, AI):
            print("AI Wins! (O)")
            break
        elif is_board_full(board):
            print("It's a Draw!")
            break

# Start the game
play_game()