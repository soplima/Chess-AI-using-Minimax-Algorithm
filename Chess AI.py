import chess
import random

# The evaluation function assigns a score to a given board position
def evaluate_board(board):
    score = 0
    for piece in chess.PIECE_TYPES:
        score += len(board.pieces(piece, chess.WHITE)) - len(board.pieces(piece, chess.BLACK))
    return score

# The minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# The AI player that uses minimax to select moves
def ai_player(board, depth):
    best_move = None
    max_eval = float('-inf')
    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, float('-inf'), float('inf'), False)
        board.pop()
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move

# The random player that selects a move at random
def random_player(board):
    return random.choice(list(board.legal_moves))

# The main game loop
def play_game(ai_depth):
    board = chess.Board()
    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = ai_player(board, ai_depth)
            print('AI player move:', move)
        else:
            move = random_player(board)
            print('Random player move:', move)
        board.push(move)
    print(board.result())

# Play a game with the AI player at depth 3
play_game(3)
