import re

def validate_board(board):
    '''
    This function checks that a valid board is sent as input
    '''
    if len(board) == 9 and valid_characters(board):
        return True

def valid_characters(strg):
    pass

def check_full_board(board):
    '''
    This function checks for a full board
    param: board
    return: boolean
    '''
    return ' ' not in board

def check_winner(board, player):
    pass

def check_winning_player(board):
    pass