from logic import check_winner

def get_empty_board():
    """
    Returns an empty 3x3 board.
    """
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def get_player_input(current_player):
    """
    Prompt the current player for their move and return it as (row, col).
    """
    while True:
        try:
            move = input(f"Player {current_player}, please enter your move (row,col): ")
            row, col = map(int, move.split(','))
            return row, col
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

def switch_player(current_player):
    """
    Toggle between 'X' and 'O'.
    """
    return 'O' if current_player == 'X' else 'X'

def print_board(board):
    """
    Print the Tic-Tac-Toe board.
    """
    for row in board:
        print(' '.join([cell if cell is not None else ' ' for cell in row]))

if __name__ == '__main':
    current_player = 'X'
    board = get_empty_board()
    winner = None

    while winner is None:
        print_board(board)
        try:
            row, col = get_player_input(current_player)
        except ValueError:
            continue

        if board[row][col] is None:
            board[row][col] = current_player
            winner = check_winner(board)
            if winner is not None:
                print(f"Player {current_player} wins!")
            else:
                current_player = switch_player(current_player)
        else:
            print("That position is already occupied. Try again.")

    print_board(board)