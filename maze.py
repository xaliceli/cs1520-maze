"""
File: maze.py
Defines a Grid-based Maze class.
"""

from arrays import Array
from stack import ArrayStack
from grid import Grid


class Maze(Grid):
    """
    Represents a two-dimensional maze.
    """

    def __init__(self, rows, columns, data, start="P", end="T", path=" "):
        Grid.__init__(self, rows, columns)
        self._start = start
        self._end = end
        self._path = path
        for row in range(rows):
            self._data[row] = Array(columns, None)
            for col in range(columns):
                self._data[row][col] = data[row + 2][col]

    def setCoord(self, row, column, value):
        """
        Set the value at a pair of coordinates.
        Precondition:
            row and column are integers between 0 and grid dimensions.
        Postcondition:
            Maze cell at row and column set to new value.
        Raises:
            ValueError if coordinates exceed maze dimensions.
            ValueError if coordinates are less than 0.
            TypeError if coordinates are not integers.
        """
        if isinstance(row, int) and isinstance(column, int):
            if row >= 0 and column >= 0:
                if row <= self.getHeight() and column <= self.getWidth():
                    self._data[row][column] = value
                else:
                    errorMsg = """Coordinates must be less than or equal to maze
                               dimensions."""
                    raise ValueError(errorMsg)
            else:
                errorMsg = "Coordinates must be greater than or equal to 0."
                raise ValueError(errorMsg)
        else:
            errorMsg = "Coordinates must be integers."
            raise TypeError(errorMsg)

    def solve(self, showSolution=False):
        """
        Uses backtracking algorithm to solve maze.
        Returns "SUCCESS" or "FAILURE" if the maze can or cannot be solved.
        Optionally, prints the solved maze.
        """

        # Instantiate empty stack to record coordinates to evaluate.
        coords = ArrayStack()

        # Search for starting point.
        # Push onto coords when found.
        searching = True
        while searching:
            for row in range(self.getHeight()):
                for col in range(self.getWidth()):
                    if self._data[row][col] == self._start:
                        coords.push((row, col))
                        searching = False
                        print "Starting point found at (%d, %d)." % (row, col)
            if searching:
                raise Exception("No valid starting point found.")

        # Search for end point value until found, or until
        # no possible moves exist.
        searching = True
        while searching:
            active = coords.pop()
            if active:
                activeValue = self._data[active[0]][active[1]]
                if activeValue == self._path:
                    self.setCoord(active[0], active[1], ".")
                adjacent = findAdjacent(active[0], active[1],
                                        self.getHeight(), self.getWidth())
                for coord in adjacent:
                    if self._data[coord[0]][coord[1]] == self._end:
                        print("SUCCESS: Endpoint found at (%d, %d)." %
                              (coord[0], coord[1]))
                        if showSolution:
                            print "Solution: \n", str(self)
                        searching = False
                    elif self._data[coord[0]][coord[1]] == self._path:
                        coords.push(coord)
            else:
                print "FAILURE: No solution found."
                if showSolution:
                    print "Attempted solution: \n", str(self)
                searching = False


def findAdjacent(x, y, xbound, ybound):
    """
    For a given set of x, y coordinates, returns the adjacent coordinates.
    Assumes that coordinates cannot be negative.
    Ignores diagonal adjacencies.
    Precondition: x and y are both positive integers
                  between 0 and specified upper bounds.
    """

    adjacent = []

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i >= 0 and j >= 0 and
               i <= xbound and j <= ybound and
               not (i == x and j == y) and
               (i == x or j == y)):
                adjacent.append((i, j))

    return adjacent
