def find_winner(gridOfDiscs):
    grid = Grid(gridOfDiscs, len(gridOfDiscs))
    return grid.calculate_winner()


class Grid:
    # Represents the whole grid.
    # Takes each row and creates a GridRow class from it.
    # Loops over each GridRow to check for four in a row

    def __init__(self, gridOfDiscs, cols):
        self.grid = []
        for (index, row) in enumerate(gridOfDiscs):
            self.grid.append(
                GridRow(row, index, cols, gridOfDiscs[index + 1 : index + 4])
            )

    def calculate_winner(self):
        for row in self.grid:
            winner = row.check_four_in_a_row()
            if winner:
                return winner


class GridRow:
    # Represents a single row.
    # Includes methods to check to see if there is four in a row along row, column or diagonal.
    # Each method looks at the next four positions based on disc index/row position and checks to see if there is only one type of disc.
    # E.g. across 4 positions in a row, if there are only "R"s or "L"s, then that means it is four in a row

    def __init__(self, row, position, cols, nextThreeRows):
        self.length = len(row)
        self.position = position
        self.row = row
        self.nextThreeRows = nextThreeRows
        self.cols = cols

    # Loops each disc in a row and checks for four in a row along row, column and diagonal
    # Decides where to check four in a row based on disc position and row position in grid
    def check_four_in_a_row(self):
        for (index, disc) in enumerate(self.row):
            if disc:
                if index <= self.length - 4:
                    winner = self.check_row(index)
                    if winner:
                        return winner
                if self.position <= self.cols - 4:
                    winner = self.check_col(index, disc) or self.check_diagonal(
                        index, disc
                    )
                    if winner:
                        return winner

    # Check four in a row
    def check_row(self, index):
        types_of_discs = set(self.row[index : index + 4])
        if len(types_of_discs) == 1:
            return types_of_discs.pop()

    # Check four in a row along column
    def check_col(self, index, disc):
        types_of_discs = {disc}
        for row in self.nextThreeRows:
            types_of_discs.add(row[index])
        if len(types_of_discs) == 1:
            return types_of_discs.pop()

    # Check four in a row along left or right diagonal
    def check_diagonal(self, index, disc):
        if index == self.length - 4:
            return self.check_right_or_left_diagonal(
                disc, index, "right"
            ) or self.check_right_or_left_diagonal(disc, index, "left")
        elif index <= self.length - 4:
            return self.check_right_or_left_diagonal(disc, index, "right")
        elif index >= self.length - 4:
            return self.check_right_or_left_diagonal(disc, index, "left")

    def check_right_or_left_diagonal(self, disc, currentIndex, direction):
        types_of_discs = {disc}
        for (rowIndex, row) in enumerate(self.nextThreeRows):
            index = (
                currentIndex + 1 + rowIndex
                if direction == "right"
                else currentIndex - 1 - rowIndex
            )
            types_of_discs.add(row[index])
        if len(types_of_discs) == 1:
            return types_of_discs.pop()
