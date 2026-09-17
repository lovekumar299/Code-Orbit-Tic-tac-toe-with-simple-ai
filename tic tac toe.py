import math

# Create the board
board = [" " for _ in range(9)]


# Display the board
def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


# Check whether a player has won
def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True

    return False


# Check whether the board is full
def is_draw():
    return " " not in board


# Minimax AI algorithm
def minimax(is_maximizing):
    
    # If computer wins
    if check_winner("O"):
        return 1

    # If user wins
    if check_winner("X"):
        return -1

    # If draw
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


# Computer chooses the best move
def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


# Main game
def play_game():

    global board

    board = [" " for _ in range(9)]

    print("Welcome to AI Tic-Tac-Toe!")
    print("You are X")
    print("Computer is O")

    while True:

        print_board()

        # User's move
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move] != " ":
                print("That position is already occupied!")
                continue

            board[move] = "X"

        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check user win
        if check_winner("X"):
            print_board()
            print("Congratulations! You won!")
            break

        # Check draw
        if is_draw():
            print_board()
            print(" The game is a draw!")
            break

        # Computer's move
        print(" Computer is thinking...")

        computer_move()

        # Check computer win
        if check_winner("O"):
            print_board()
            print(" Computer wins!")
            break

        # Check draw
        if is_draw():
            print_board()
            print(" The game is a draw!")
            break


# Start the game
play_game()