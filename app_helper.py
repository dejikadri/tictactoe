import re

def validate_board(board):
    '''
    This function checks that a valid board is sent as input
    '''
    if len(board) == 9 and valid_characters(board):
        return True

def valid_characters(strg):
    '''
    This function checks that the board contains only valid characters
    '''
    search = re.compile(r'[^x o.]').search
    return not bool(search(strg))

def check_full_board(board):
    '''
    This function checks for a full board
    param: board
    return: boolean
    '''
    return ' ' not in board

def check_winner(board, player):
    if board[0] == board[1] == board[2] == player or \
        board[3] == board[4] == board[5] == player or \
        board[6] == board[7] == board[8] == player or \
        board[0] == board[3] == board[6] == player or \
        board[2] == board[5] == board[8] == player or \
        board[0] == board[4] == board[8] == player or \
        board[2] == board[4] == board[6] == player:
        return True
    else:
        return False

def check_winning_player(board):
    if check_winner(board, 'o'):
        return 'o wins'
    elif check_winner(board, 'x'):
        return 'x wins'

def get_computers_move(board, o_pos):
    '''
    This function checks the board and puts o in an optimal
    position
    '''
    for i in range(0, 8):
        if board[i] == ' ':
            return change_xter(board, i, o_pos)

def change_xter(original_string, position, xter):
    '''
    This function allows a string character to be replaced
    by specifying the position and new character.
    '''
    lst = list(original_string)
    if lst[position] == ' ':
        lst[position] = xter
        return ''.join(lst)
    else:
        return None

def is_position_empty(board, board_pos):
    return board[board_pos] == ' '