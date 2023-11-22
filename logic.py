class TicTacToeGame:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = None
        self.board = self.get_empty_board()

    def get_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def get_player_input(self):
        return self.current_player.get_move(self.board)

    def play(self):
        while self.winner is None:
            self.print_board()
        try:
            row, col = self.get_player_input()
            if self.current_player is not None:
                if self.board[row][col] is None:
                    self.board[row][col] = self.current_player.symbol
                    self.winner = self.check_winner()
                    if self.winner is not None:
                        print(f"Player {self.current_player.symbol} wins!")
                        break

                    else:
                        self.current_player = self.switch_player()
                else:
                    print("That position is already occupied. Try again.")
            else:
                print("Invalid player. Try again.")
        except ValueError:
            continue


    def check_winner(self):
        for row in self.board:
            if len(set(row)) == 1 and row[0] is not None:
                return row[0]

        for i in range(len(self.board)):
            column = [self.board[j][i] for j in range(len(self.board))]
            if len(set(column)) == 1 and column[0] is not None:
                return column[0]

        top_left_to_bottom_right = [self.board[i][i] for i in range(len(self.board))]
        if len(set(top_left_to_bottom_right)) == 1 and top_left_to_bottom_right[0] is not None:
            return top_left_to_bottom_right[0]

        top_right_to_bottom_left = [self.board[i][len(self.board) - i - 1] for i in range(len(self.board))]
        if len(set(top_right_to_bottom_left)) == 1 and top_right_to_bottom_left[0] is not None:
            return top_right_to_bottom_left[0]

        flat_board = [cell for row in self.board for cell in row]
        if None not in flat_board:
            return "Draw"

        return None

    def print_board(self):
        for row in self.board:
            print(' '.join([cell if cell is not None else ' ' for cell in row]))

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self, board):
        raise NotImplementedError("Subclasses must implement this method.")

class HumanPlayer(Player):
    def get_move(self, board):
        while True:
            try:
                move = input(f"{self.name}, please enter your move (row,col): ")
                row, col = map(int, move.split(','))
                return row, col
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

class BotPlayer(Player):
    def get_move(self, board):
        empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
        return random.choice(empty_positions)

if __name__ == "__main__":
    player1 = HumanPlayer("Player 1", "X")
    player2 = BotPlayer("Bot", "O")

    game = TicTacToeGame(player1, player2)
    game.play()