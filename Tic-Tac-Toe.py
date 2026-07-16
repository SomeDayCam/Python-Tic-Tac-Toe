import random

start, end = 1, 9
playerMoveRecord = "Your move is recorded"
computerMoveRecord = "Now the computer will play"
gameState = ""
spacer = "   "
boardPlays = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]

# outputs the current state of the tic-tac-toe board
def ticTacToeBoard():
    boardOutput = ""
    count = 1
    for position in boardPlays:
        boardOutput = boardOutput + position + spacer
        if count == 3 or count == 6:
            boardOutput = boardOutput + "\n"
        count += 1
    return boardOutput

# checks if the game has been won or lost
def did_i_win_or_lose(boardPlays):
    for n in WIN_LINES:
        if boardPlays[n[0]] == boardPlays[n[1]] == boardPlays[n[2]] == "X":
            return "Win"
        elif boardPlays[n[0]] == boardPlays[n[1]] == boardPlays[n[2]] == "O":
            return "Lose"
    return "Unknown"

# returns list of the remaining moves that are available
def remaining_moves():
    movesAvailable = []
    for position in boardPlays:
        if position != "X" and position != "O":
            movesAvailable.append(int(position) - 1)
    return movesAvailable

# asks the player for a move and keeps asking until it is valid,
# then returns it as a board index (0 - 8)
def get_player_move():
    playerMovestring = input("Enter the position where you want to play >>")
    validMove = False
    while validMove == False:
        if not playerMovestring.isdigit():
            playerMovestring = input("That was not a number, try again >>")
        elif not (start <= int(playerMovestring) <= end):
            playerMovestring = input("Your move was not within the range 1 - 9, try again >>")
        elif boardPlays[int(playerMovestring) - 1] == "X" or boardPlays[int(playerMovestring) - 1] == "O":
            playerMovestring = input("You cannot make a play in that position, choose another >>")
        else:
            validMove = True
    return int(playerMovestring) - 1

# if the computer is 1 move away from winning, it will be forced to make the winning play
# instead of using a random un-occupied position
def computer_win_move(boardPlays):
    for n in WIN_LINES:
        if (boardPlays[n[0]] == boardPlays[n[1]] == "O") and boardPlays[n[2]] != "X":
            return n[2]
        elif (boardPlays[n[0]] == boardPlays[n[2]] == "O") and boardPlays[n[1]] != "X":
            return n[1]
        elif (boardPlays[n[1]] == boardPlays[n[2]] == "O") and boardPlays[n[0]] != "X":
            return n[0]
    return random.choice(remaining_moves())

# Priming Input
print(ticTacToeBoard())
playerMove = get_player_move()
boardPlays[playerMove] = "X"

# Game Loop
while gameState == "":
    result = did_i_win_or_lose(boardPlays)

    # if the game is not decided, the computer makes a move
    if result == "Unknown" and len(remaining_moves()) > 0:
        print(f"{playerMoveRecord}\n{ticTacToeBoard()}\n\n{computerMoveRecord}")
        boardPlays[computer_win_move(boardPlays)] = "O"
        print(ticTacToeBoard())
        result = did_i_win_or_lose(boardPlays)

    # if the game is still not decided, the player makes a move
    if result == "Unknown" and len(remaining_moves()) > 0:
        playerMove = get_player_move()
        boardPlays[playerMove] = "X"
        print(f"{playerMoveRecord}\n{ticTacToeBoard()}")
        result = did_i_win_or_lose(boardPlays)

    # end-of-round check: win, lose, or tie
    if result != "Unknown":
        gameState = result
        if result == "Win":
            print("You Win!")
        else:
            print("You Lose!")
    elif len(remaining_moves()) == 0:
        gameState = "Tie"
        print("It is a tie! No one won or lost!")
