from logic import check_winner

boards = [
    [
        ['O', '1', 'O'],
        ['O', '1', 'O'],
        ['O', 'O', '1'],
    ],
    [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ],
    [
        ['O', None, None],
        [None, 'X', None],
        [None, None, None],
    ],
]

for idx, board in enumerate(boards):
    winner = check_winner(board)
    print(f"{idx}: {winner}")