def find_winner(grid):
    grid = Grid(grid, len(grid))
    return grid.calculate_winner()


class Grid:
    def __init__(self, grid, cols):
        self.grid = []
        for (index, row) in enumerate(grid):
            self.grid.append(GridRow(row, index, cols, grid[index + 1 : index + 4]))

    def calculate_winner(self):
        for row in self.grid:
            winner = row.calculate_winner()
            if winner:
                return winner


class GridRow:
    def __init__(self, row, position, cols, nextThreeRows):
        self.length = len(row)
        self.position = position
        self.row = row
        self.nextThreeRows = nextThreeRows
        self.cols = cols

    def calculate_winner(self):
        for (index, disc) in enumerate(self.row):
            if disc:
                if index <= self.length - 4:
                    winner = self.match_row(index)
                    if winner:
                        return winner
                if self.position <= self.cols - 4:
                    winner = self.match_col(index, disc) or self.match_diagonal(
                        index, disc
                    )
                    if winner:
                        return winner

    def match_row(self, index):
        matching_discs = set(self.row[index : index + 4])
        if len(matching_discs) == 1:
            return matching_discs.pop()

    def match_col(self, index, disc):
        matching_discs = {disc}
        for row in self.nextThreeRows:
            matching_discs.add(row[index])
            print(row[index], index, self.nextThreeRows, self.position, self.row)
        if len(matching_discs) == 1:
            return matching_discs.pop()

    def match_diagonal(self, index, disc):
        if index < 3:
            return self.match_right_or_left_diagonal(disc, index, "right")
        elif index > 2:
            return self.match_right_or_left_diagonal(disc, index, "left")

    def match_right_or_left_diagonal(self, disc, currentPos, dir):
        matching_discs = {disc}
        for (rowIndex, row) in enumerate(self.nextThreeRows):
            index = (
                currentPos + 1 + rowIndex
                if dir == "right"
                else currentPos - 1 - rowIndex
            )
            matching_discs.add(row[index])
        if len(matching_discs) == 1:
            return matching_discs.pop()
