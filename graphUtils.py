"""
Helpfull function to work with graphs
"""


def hasPredecessor(indexVertice, adjencyMatrix):
    """Function that check if a vertice has predecessor"""
    for i in range(len(adjencyMatrix[0])):
        if (adjencyMatrix[i][indexVertice]):
            return True
    return False


def removeEntryPointFromMatrix(entryPointList, adjencyMatrix, verticeList):
    """Function to remove vertices from adjency matrix"""
    # Removing entry points
    for line in adjencyMatrix:
        for point in reversed(entryPointList):
            del line[point]

    for point in reversed(entryPointList):
        del verticeList[point]
        del adjencyMatrix[point]

    return adjencyMatrix, verticeList
