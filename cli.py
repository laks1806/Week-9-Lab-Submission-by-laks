from logic import TicTacToeGame
from logic import BotPlayer, HumanPlayer


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
            move = input(f"Player {current_player.name}, please enter your move (row,col): ")
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


if __name__ == '__main__':
    # Create an instance of the TicTacToeGame class
    game = TicTacToeGame(HumanPlayer('Player 1', 'X'), HumanPlayer('Player 2', 'O'))

    # Play the game
    while game.winner is None:
        print_board(game.board)

        # Get the player's move
        row, col = get_player_input(game.current_player)

        # Make the move
        game.board[row][col] = game.current_player.symbol

        # Check for a winner
        game.winner = game.check_winner()

        # Switch players
        game.switch_player()

    # Print the final board and winner
    print_board(game.board)
    print(f"Player {game.winner} wins!")
