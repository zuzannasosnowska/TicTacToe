import random

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

movement_List = []
##game_still_going = True
player = "X"
winner = None


def show_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def game():
    while True:
        movement = int(input("Make your move! "))
        if movement in movement_List:
            print("This position is already taken. Try again")
        else:
            movement_List.append(movement)
            board[movement] = "X"
            check_winner()
            if winner == "X":
                print(winner + " won")
                show_board()
                break
            elif check_if_tie() == True:
                print("It's a tie")
                show_board()
                break
            comp_move = random.choice([num for num in range(0, 9) if num not in movement_List])
            print(comp_move)
            movement_List.append(comp_move)
            board[comp_move] = "O"
            check_winner()
            if winner == "O":
                print(winner + " won")
                show_board()
                break
            elif check_if_tie() == True:
                print("its a tie")
                show_board()
                break

            show_board()


def check_winner():
    global winner
    row_win = check_rows()
    diag_win = check_diagonal()
    col_win = check_columns()
    tie_win = check_if_tie()

    if row_win:
        winner = row_win
    elif col_win:
        winner = col_win
    elif diag_win:
        winner = diag_win
    elif tie_win:
        winner = tie_win


def check_rows():
    ##global game_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        if row1:
            ##game_still_going = False
            return board[0]
            # print("Player " + board[0]+" won")
        elif row2:
            ##game_still_going = False
            return board[3]
            # print("Player " + board[3] + " won")
        elif row3:
            ##game_still_going = False
            return board[6]
            # print("Player " + board[6] + " won")
        else:
            return None


def check_columns():
    ##global game_still_going
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        if col1:
            ##game_still_going = False
            return board[0]
            # print("Player " + board[0]+" won")
        elif col2:
            ##game_still_going = False
            return board[1]
            # print("Player " + board[1] + " won")
        elif col3:
            ##game_still_going = False
            return board[2]
            # print("Player " + board[2] + " won")
        else:
            return None


def check_diagonal():
    ##global game_still_going
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[6] == board[4] == board[2] != "-"
    if diag1 or diag2:
        if diag1:
            ##game_still_going = False
            return board[0]
            # print("Player " + board[0]+" won")
        elif diag2:
            ##game_still_going = False
            return board[6]
            # print("Player " + board[6] + " won")
        else:
            return None


def check_if_tie():
    ##global game_still_going
    if "-" not in board:
        ##game_still_going = False
        # print("Its a tie")
        return True
    else:
        return False


game()