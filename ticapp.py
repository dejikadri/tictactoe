from flask import Flask, jsonify, make_response, request

import app_helper as hlp


app = Flask(__name__)

@app.route('/')
def index():
    """
        Processes board for validity and moves
        :return: a sequence of strings representing a tic tac toe board
    """
    board = request.args.get('board', default=1, type=str)

    if hlp.validate_board(board):
        winner = hlp.check_winning_player(board)
        if winner == 'x' or winner == 'o' or winner == 'tie' :
            return winner + ' wins'
        else:
            return hlp.get_computers_play(board, 'o')

    else:
        return jsonify({'Error': '400 (Bad Request)'})