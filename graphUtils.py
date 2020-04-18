"""
Helpfull function to work with graphs
"""


def hasPredecessor(indexVertice, adjencyMatrix):
    """Private function that check if a vertice has predecessor"""
    for i in range(len(adjencyMatrix[0])):
        if (adjencyMatrix[i][indexVertice]):
            return True
    return False


def removeEntryPointFromMatrix(entryPointList, adjencyMatrix, verticeList):
    # Removing entry points
    for line in adjencyMatrix:
        for point in reversed(entryPointList):
            del line[point]

    for point in reversed(entryPointList):
        del verticeList[point]
        del adjencyMatrix[point]

    return adjencyMatrix, verticeList
