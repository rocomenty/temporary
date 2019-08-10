class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def checkAdjacent(click):
            nonlocal board
            count = 0
            for row in range(max(0, click[0] - 1), min(len(board), click[0] + 2)):
                for col in range(max(0, click[1] - 1), min(len(board[0]), click[1] + 2)):
                    if row == click[0] and col == click[1]:
                        continue
                    if board[row][col] == 'M':
                        count += 1
            return count

        # if a mine is revealed case
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        # if an empty square is revealed no adjacent mines
        # or had adjacent mines
        def updateRecursive(click):
            nonlocal board
            adjacentMines = checkAdjacent(click)
            if adjacentMines == 0:
                board[click[0]][click[1]] = 'B'
                for row in range(max(0, click[0] - 1), min(len(board), click[0] + 2)):
                    for col in range(max(0, click[1] - 1), min(len(board[0]), click[1] + 2)):
                        if (row == click[0] and col == click[1]):
                            continue
                        if board[row][col] == 'E':
                            updateRecursive([row, col])
            else:
                board[click[0]][click[1]] = str(adjacentMines)

        updateRecursive(click)
        return board
