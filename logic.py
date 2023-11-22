import random


class TicTacToeGame:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = player1
        self.board = self.get_empty_board()
        self.winner = None

    def get_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def get_player_input(self):
        while True:
            try:
                row, col = map(int, input(f"{self.current_player.name}, please enter your move (row,col): ").split(','))
                if 0 <= row < 3 and 0 <= col < 3:
                    return row, col
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

    def play(self):
        while self.winner is None:
            self.print_board()

            try:
                row, col = self.get_player_input()
                if self.board[row][col] is None:
                    self.board[row][col] = self.current_player.symbol
                    self.winner = self.check_winner()

                    if self.winner is not None:
                        print(f"Player {self.current_player.symbol} wins!")
                        return

                    self.switch_player()
                else:
                    print("That position is already occupied. Try again.")
            except ValueError:
                pass

            if None not in [cell for row in self.board for cell in row]:
                self.winner = "Draw"
                print("It's a tie!")

    def check_winner(self):
        for row in self.board:
            if len(set(row)) == 1 and row[0] is not None:
                return row[0]

        for col in range(3):
            column = [self.board[i][col] for i in range(3)]
            if len(set(column)) == 1 and column[0] is not None:
                return column[0]

        top_left_to_bottom_right = [self.board[i][i] for i in range(3)]
        if len(set(top_left_to_bottom_right)) == 1 and top_left_to_bottom_right[0] is not None:
            return top_left_to_bottom_right[0]

        top_right_to_bottom_left = [self.board[i][3 - i - 1] for i in range(3)]
        if len(set(top_right_to_bottom_left)) == 1 and top_right_to_bottom_left[0] is not None:
            return top_right_to_bottom_left[0]
        
        empty_positions = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
        if len(empty_positions) == 0:
            return "Draw"
        return None

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join([str(cell) if cell is not None else ' ' for cell in row]) + ' |')


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self, board):
        raise NotImplementedError("Subclasses must implement this method.")


class HumanPlayer(Player):
    def get_move(self, board):
        return self.get_player_input()

    def get_player_input(self):
        while True:
            try:
                row, col = map(int, input(f"{self.name}, please enter your move (row,col): ").split(','))
                return row, col
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")


class BotPlayer(Player):
    def get_move(self, board):
        empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
