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


def hasPredecessor(indexVertice, adjencyMatrix) -> bool:
    """Function that check if a vertice has predecessor"""
    for i in range(len(adjencyMatrix[0])):
        if (adjencyMatrix[i][indexVertice]):
            return True
    return False


def removeEntryPointFromMatrix(entryPointList, adjencyMatrix, verticeList) -> tuple:
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


########################
#     Earlyest Time    #
########################


def getEarlyestDate(valueMatrix, ranks) -> list:
    """Function that compute the earliest date for every vertices"""
    earliestDate = [0] * len(ranks)
    for rank in range(max(ranks)):
        for rankId in range(1, len(ranks)):
            if (ranks[rankId] == rank):
                earlDateVertice = getEarlyestDatePred(
                    rankId, valueMatrix, earliestDate)
                earliestDate[rankId] = earlDateVertice
        earliestDate[-1] = getEarlyestDatePred(rankId,
                                               valueMatrix, earliestDate)
    return earliestDate


def getEarlyestDatePred(vertice, valueMatrix, earliestDate):
    predecessors = getPredecessorId(vertice, valueMatrix)
    listAllPredDate = []
    for i in predecessors:
        listAllPredDate.append(valueMatrix[i][vertice] + earliestDate[i])
    return max(listAllPredDate)


def getPredecessorId(vertice, valueMatrix):
    pred = []
    for i in range(len(valueMatrix[0])):
        if (valueMatrix[i][vertice] != None):
            pred.append(i)
    return pred


########################
#      Latest Time     #
########################


def getLatestDate(valueMatrix, ranks, maxDate) -> list:
    """Function that compute the earliest date for every vertices"""
    latestDate = [0] * len(ranks)
    latestDate[-1] = maxDate
    for rank in range(max(ranks) -1, 0, -1):
        for rankId in range(1, len(ranks)):
            if (ranks[rankId] == rank):
                earlDateVertice = getLatestDatePred(
                    rankId, valueMatrix, latestDate)
                latestDate[rankId] = earlDateVertice
    return latestDate


def getLatestDatePred(vertice, valueMatrix, latestDate):
    successors = getSuccessorId(vertice, valueMatrix)
    listAllSuccDate = []
    for i in successors:
        listAllSuccDate.append(latestDate[i] - valueMatrix[vertice][i])
    return min(listAllSuccDate)


def getSuccessorId(vertice, valueMatrix):
    succ = []
    for i in range(len(valueMatrix[vertice])):
        if (valueMatrix[vertice][i] != None):
            succ.append(i)
    return succ
