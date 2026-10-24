"""Tic-tac-toe game with an Alpha-Beta computer opponent."""

from math import inf

Board = list[str]
HUMAN = "X"
COMPUTER = "O"
EMPTY = " "


def available_moves(board: Board) -> list[int]:
    """Return the indexes of the empty squares."""
    return [index for index, cell in enumerate(board) if cell == EMPTY]


def winner(board: Board) -> str | None:
    """Return the winning mark, or None if there is no winner."""
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]

    for first, second, third in lines:
        if board[first] == board[second] == board[third] != EMPTY:
            return board[first]

    return None


def minimax(
    board: Board,
    maximizing: bool,
    alpha: float = -inf,
    beta: float = inf,
) -> int:
    """Score the board using Minimax with Alpha-Beta pruning."""
    game_winner = winner(board)

    if game_winner == COMPUTER:
        return 1
    if game_winner == HUMAN:
        return -1
    if not available_moves(board):
        return 0

    if maximizing:
        best_score = -inf
        for move in available_moves(board):
            board[move] = COMPUTER
            score = minimax(board, False, alpha, beta)
            board[move] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return int(best_score)

    best_score = inf
    for move in available_moves(board):
        board[move] = HUMAN
        score = minimax(board, True, alpha, beta)
        board[move] = EMPTY
        best_score = min(best_score, score)
        beta = min(beta, best_score)
        if beta <= alpha:
            break
    return int(best_score)


def best_computer_move(board: Board) -> int:
    """Choose the best available square for the computer."""
    best_score = -inf
    chosen_move = -1

    for move in available_moves(board):
        board[move] = COMPUTER
        score = minimax(board, False)
        board[move] = EMPTY

        if score > best_score:
            best_score = score
            chosen_move = move

    return chosen_move


def display_board(board: Board) -> None:
    """Print the board, using 1–9 to label empty squares."""
    cells = [
        str(index + 1) if cell == EMPTY else cell
        for index, cell in enumerate(board)
    ]

    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]}")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]}")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]}")
    print()


def play() -> None:
    """Play a console game against the computer."""
    board = [EMPTY] * 9
    print("Tres en raya: tú eres X y la computadora es O.")

    while True:
        display_board(board)

        try:
            move = int(input("Elige una casilla del 1 al 9: ")) - 1
        except ValueError:
            print("Escribe un número del 1 al 9.")
            continue

        if move not in available_moves(board):
            print("Esa casilla no está disponible. Intenta otra.")
            continue

        board[move] = HUMAN

        if winner(board) == HUMAN:
            display_board(board)
            print("¡Ganaste!")
            break
        if not available_moves(board):
            display_board(board)
            print("Empate.")
            break

        computer_move = best_computer_move(board)
        board[computer_move] = COMPUTER
        print(f"La computadora eligió la casilla {computer_move + 1}.")

        if winner(board) == COMPUTER:
            display_board(board)
            print("Ganó la computadora.")
            break
        if not available_moves(board):
            display_board(board)
            print("Empate.")
            break


if __name__ == "__main__":
    play()