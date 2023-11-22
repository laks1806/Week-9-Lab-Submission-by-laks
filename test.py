import unittest
from logic import TicTacToeGame, HumanPlayer, BotPlayer


class TicTacToeGameTest(unittest.TestCase):

    def setUp(self):
        self.player1 = HumanPlayer("Player 1", "X")
        self.player2 = BotPlayer("Bot", "O")
        self.game = TicTacToeGame(self.player1, self.player2)

    def test_get_empty_board(self):
        empty_board = self.game.get_empty_board()
        self.assertEqual(empty_board, [[None, None, None], [None, None, None], [None, None, None]])

    def test_check_winner_with_row_win(self):
        self.game.board = [[None, None, None], ["X", "X", "X"], [None, None, None]]
        self.assertEqual(self.game.check_winner(), "X")

    def test_check_winner_with_column_win(self):
        self.game.board = [[None, "O", None], [None, "O", None], ["O", "O", "O"]]
        self.assertEqual(self.game.check_winner(), "O")

    def test_check_winner_with_diagonal_win(self):
        self.game.board = [["X", None, None], ["O", "X", None], ["O", "O", "X"]]
        self.assertEqual(self.game.check_winner(), "X")

    def test_check_winner_with_draw(self):
        self.game.board = [["X", "O", "X"], ["X", "O", "X"], ["O", "X", "O"]]
        self.assertEqual(self.game.check_winner(), "Draw")

    def test_play_game(self):
        self.game.play()
        self.assertTrue(self.game.winner is not None)


if __name__ == "__main__":

    test_result = unittest.main()
    print("----------------------------------------------------------------")
    print("Test Results:")
    print("----------------------------------------------------------------")
    print("Passed:", test_result.testsPassed)
    print("Failed:", test_result.failures)
    print("Errors:", test_result.errors)


