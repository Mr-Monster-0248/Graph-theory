"""
Helpfull function to work with graphs
"""


def printMatrix(matrix):
    print("\t", end='')
    for i in range(len(matrix[0])):
        print(str(i) + "\t", end='')
    print('')
    for i in range(len(matrix)):
        print(str(i) + '\t', end='')
        for value in matrix[i]:
            if (value == None or value == False):
                print(".\t", end='')
            else:
                print(str(value) + '\t', end='')
        print('')
    print()


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


def getEntryPointNumber(ranks: list) -> int:
    """Return the number of vertices with rank 0"""
    return ranks.count(0)


def getEndPointNumber(ranks: list) -> int:
    """Return the number of vertices with the maximum rank"""
    return ranks.count(max(ranks))


def hasNegativeEdge(valueMatrix) -> bool:
    """Locate if any edges has a negative value"""
    for line in valueMatrix:
        for value in line:
            if (value != None):
                if (value < 0):
                    return True
    return False


def hasSameValueEdges(valueCheked, verticeIndex, valueMatrix) -> bool:
    """Check that a vertice has outgoing edges with the same checked value"""
    for value in valueMatrix[verticeIndex]:
        if (value != valueCheked and value != None):
            return False
    return True


def hasSameWeight(valueMatrix) -> bool:
    """Check for every vertices that they have same weight edges"""
    for i in range(len(valueMatrix)):
        checkedVal = findFirstEdgeValue(valueMatrix[i])
        if (not hasSameValueEdges(checkedVal, i, valueMatrix)):
            return False
    return True


def findFirstEdgeValue(edgeList) -> int:
    """Function to find the first non None value in the edge list"""
    for edge in edgeList:
        if (edge != None):
            return edge
    else:
        return -1
