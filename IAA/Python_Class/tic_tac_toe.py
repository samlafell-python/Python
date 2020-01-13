tic_tac_toe = {'A1': ' ', 'B1': ' ', 'C1': ' ', 'A2': ' ', 'B2': ' ', 'C2': ' ',
               'A3': ' ', 'B3': ' ', 'C3': ' '}

while True:
    print('Welcome to Tic-Tac-Toe! Player 1, please enter your name. (blank to quit)')
    player1name = input()
    if player1name == '':
        break
    print('Welcome, ' + player1name + '. You will be X')
    print('Player 2, please enter your name')
    player2name = input()
    print('Welcome, ' + player2name + '. You will be O')
    break


def board(board):
    print(tic_tac_toe['A1'] + '|' + tic_tac_toe['B1'] + '|' + tic_tac_toe['C1'])
    print('------')
    print(tic_tac_toe['A2'] + '|' + tic_tac_toe['B2'] + '|' + tic_tac_toe['C2'])
    print('------')
    print(tic_tac_toe['A3'] + '|' + tic_tac_toe['B3'] + '|' + tic_tac_toe['C3'])


def win_check(tic_tac_toe):
    if tic_tac_toe['A1'] == 'X' and tic_tac_toe['A2'] == 'X' and tic_tac_toe['A3'] == 'X':
        global win
        win = 1
        return print(player1name, 'wins!')
    elif tic_tac_toe['B1'] == 'X' and tic_tac_toe['B2'] == 'X' and tic_tac_toe['B3'] == 'X':
        win = 1
        return print(player1name, 'wins!')
    elif tic_tac_toe['C1'] == 'X' and tic_tac_toe['C2'] == 'X' and tic_tac_toe['C3'] == 'X':
        win = 1
        return print(player1name, 'wins!')
    elif tic_tac_toe['A1'] == 'X' and tic_tac_toe['B2'] == 'X' and tic_tac_toe['C3'] == 'X':
        win = 1
        return print(player1name, 'wins!')
    elif tic_tac_toe['A1'] == 'X' and tic_tac_toe['B1'] == 'X' and tic_tac_toe['C1'] == 'X':
        win = 1
        return print(player1name, 'wins!')
    elif tic_tac_toe['A1'] == 'X' and tic_tac_toe['B1'] == 'X' and tic_tac_toe['C1'] == 'X':
        win = 1
        return print(player1name, 'wins!')
    elif tic_tac_toe['A2'] == 'X' and tic_tac_toe['B2'] == 'X' and tic_tac_toe['C2'] == 'X':
        win = 1
        return print(player1name, 'wins!')
    elif tic_tac_toe['A3'] == 'X' and tic_tac_toe['B3'] == 'X' and tic_tac_toe['C3'] == 'X':
        win = 1
        return print(player1name, 'wins!')
    elif tic_tac_toe['A3'] == 'X' and tic_tac_toe['B2'] == 'X' and tic_tac_toe['C1'] == 'X':
        win = 1
        return print(player1name, 'wins!')
    elif tic_tac_toe['A1'] == 'O' and tic_tac_toe['A2'] == 'O' and tic_tac_toe['A3'] == 'O':
        win = 1
        return print(player2name, 'wins!')
    elif tic_tac_toe['B1'] == 'O' and tic_tac_toe['B2'] == 'O' and tic_tac_toe['B3'] == 'O':
        win = 1
        return print(player2name, 'wins!')
    elif tic_tac_toe['C1'] == 'O' and tic_tac_toe['C2'] == 'O' and tic_tac_toe['C3'] == 'O':
        win = 1
        return print(player2name, 'wins!')
    elif tic_tac_toe['A1'] == 'O' and tic_tac_toe['B2'] == 'O' and tic_tac_toe['C3'] == 'O':
        win = 1
        return print(player2name, 'wins!')
    elif tic_tac_toe['A1'] == 'O' and tic_tac_toe['B1'] == 'O' and tic_tac_toe['C1'] == 'O':
        win = 1
        return print(player2name, 'wins!')
    elif tic_tac_toe['A2'] == 'O' and tic_tac_toe['B2'] == 'O' and tic_tac_toe['C2'] == 'O':
        win = 1
        return print(player2name, 'wins!')
    elif tic_tac_toe['A3'] == 'O' and tic_tac_toe['B3'] == 'O' and tic_tac_toe['C3'] == 'O':
        win = 1
        return print(player2name, 'wins!')
    elif tic_tac_toe['A3'] == 'O' and tic_tac_toe['B2'] == 'O' and tic_tac_toe['C1'] == 'O':
        win = 1
        return print(player2name, 'wins!')


board(board)

turn = 'X'
win = 0
for num in range(9):
    if win:
        break
    print('Turn for ', turn + '. Which space would you like?' +
          ' Type A1 for top-left and C3 for bottom-right.')
    move = input()
    while move not in tic_tac_toe.keys():
        print('I did not get that. Could you enter a valid value between A1 and C3.')
        move = input()
    while tic_tac_toe[move] != ' ':
        print('Try a space that has not been taken.')
        board(board)
        move = input()
    tic_tac_toe[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    board(board)
    if win_check(tic_tac_toe):
        break

if not win:
    print('It was a tie!')