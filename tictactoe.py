def print_board(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

board = ["1","2","3","4","5","6","7","8","9"]

current_player = "X"

for turn in range(9):
    print_board(board)

    move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1

    if board[move] not in ["X", "O"]:
        board[move] = current_player
    else:
        print("Position already taken!")
        continue

    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            print_board(board)
            print(f"Player {current_player} wins!")
            exit()

    current_player = "O" if current_player == "X" else "X"

print_board(board)
print("It's a draw!")
