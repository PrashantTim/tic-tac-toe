def players():  # taking players name
    player1 = input("enter first player name: ")
    player2 = input("enter ssecond player name: ")
    return [player1, player2]


def choice(p):  # taking choice only x or o
    player = ""
    while True:
        if player != "x" and player != "o":
            print("choice need to be only x or o")
            player = input(f"player {p} choice")
        else:
            print(f"player {p} choice is {player}")
            break
    return player


def move(moves, cell):  # for the player move and keep record of the move in moves
    move_success = False
    while True:
        mov = int(input("enter number between 1 to 9 : "))
        for i in range(10):
            if (mov < 1) or (mov > 9):
                print("try again invalid move enter remaining cell number from 1 to 9")
                break
            if 'x' in cell[mov] or 'o' in cell[mov]:
                print("try again invalid move enter remaining cell number from 1 to 9")
                break
            else:
                move_success = True
                break
        if move_success == True:
            moves.append(mov)
            return mov


def game_board(cell):  # designing game board
    print(' ' + cell[1] + " | " + cell[2] + " | " + cell[3])
    print("---+---+---")
    print(' ' + cell[4] + " | " + cell[5] + " | " + cell[6])
    print("---+---+---")
    print(' ' + cell[7] + " | " + cell[8] + " | " + cell[9])


def win_logic(cell, char):
    if ((cell[1] == cell[2] == cell[3] == char)  # 1st three for rows
            or (cell[4] == cell[5] == cell[6] == char)
            or (cell[7] == cell[8] == cell[9] == char)
            or (cell[1] == cell[4] == cell[7] == char)  # next three for columns
            or (cell[2] == cell[5] == cell[8] == char)
            or (cell[3] == cell[6] == cell[9] == char)
            or (cell[1] == cell[5] == cell[9] == char)  # last two for diagonals
            or (cell[3] == cell[5] == cell[7] == char)):
        return True
    else:
        return False


def main():
    p = players()
    first_choice = choice(p[0])
    if first_choice == 'x':
        second_choice = 'o'
    else:
        second_choice = 'x'
    print(f"{p[1]} choice is {second_choice}")
    while True:  # for playing again loop
        moves = []  # for 9 moves only
        cell = [' ' for i in range(10)]  # for cell of tic tac toe discarding cell[0] for easy input
        game_board(cell)
        for i in range(9):  # for players move
            # player1 move
            print(f"player {p[0]} move")
            m = move(moves, cell)
            cell[m] = first_choice
            game_board(cell)
            w = win_logic(cell, first_choice)
            moves_length = len(moves)
            if w == True:
                print(f"congratulation {p[0]} have won the game")
                break
            if moves_length == 9:
                print(f"game draw")
                break
            print(f"player {p[1]} move")
            m = move(moves, cell)
            cell[m] = second_choice
            game_board(cell)
            w = win_logic(cell, second_choice)
            if w == True:
                print(f"congratulation {p[1]} have won the game")
                break
            moves_length = len(moves)
            if moves_length == 9:
                print(f"game draw")
                break
        play = input("do you wanna play again y/n : ")
        if not play == 'y':
            break


if __name__ == '__main__':
    main()
