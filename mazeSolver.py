"""
File: mazeSolver.py
Solves text-based mazes.
"""

from maze import Maze


def readMaze(file):
    """
    Converts a text file into a Maze object.
    Preconditions:
        First two values represent the number of rows and columns respectively.
        Number of characters after first two equals rows * columns.
    Raises:
        Exception if maze dimensions do not match number of characters in maze.
        IOError if file containing maze cannot be found.
        ValueError if first two characters in file are not integer dimensions.
    """

    try:
        with open(file) as maze:
            mazeData = maze.read().splitlines()

        numRow = int(mazeData[0])
        numCol = int(mazeData[1])

        if sum(len(i) for i in mazeData[2:]) == numRow * numCol:
            maze = Maze(rows=numRow, columns=numCol, data=mazeData)
            print "Read %s as maze." % file
            return maze
        else:
            errorMsg = "Number of characters do not match maze dimensions."
            raise Exception(errorMsg)
    except IOError:
        print "Input file not found."
    except ValueError:
        print "First 2 characters must be integer maze dimensions."


def mazeSolver(input=True, fileArg=None):
    """
    Solves a text-based maze.
    By default, prompts user to specify the name of a maze file.
    Can also pass through maze files as arguments directly,
    e.g. mazeSolver(False, "maze1.txt")
    """

    if input:
        file = raw_input("File containing maze to be solved, e.g. maze1.txt):")
    else:
        file = fileArg
    print "Reading %s." % file
    maze = readMaze(file)
    print "Unsolved Maze:"
    print str(maze)
    maze.solve(showSolution=True)


# mazeSolver()

# For testing:
numMazes = 8
for mazeIndex in range(1, numMazes + 1):
    fileName = "maze%d.txt" % mazeIndex
    print "=" * 80
    try:
        mazeSolver(False, fileName)
    except Exception, e:
        print "Error: %s \n" % e
        continue
