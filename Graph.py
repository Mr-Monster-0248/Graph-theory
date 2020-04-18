from inputs import readGraphFromFile


def hasPredecessor(vertice, adjencyMatrix):
    for line in adjencyMatrix:
        if (line[vertice]):
            return True
    return False


class Graph:
    """
    Class of a graph, defined by:
    - vertice number
    - edge number
    - list of all the edges with there values as
        [in, out, value]
    """

    def __init__(self, **keys):
        """Constructor of Graph class"""
        if ("filename" in keys):
            temp = readGraphFromFile(keys['filename'])
            self.verticeNumber = temp[0]
            self.edgeNumber = temp[1]
            self.edgeList = temp[2]
        elif (verticeNumber in keys and edgeNumber in keys and edgeList in keys):
            self.verticeNumber = keys['verticeNumber']
            self.edgeNumber = keys['edgeNumber']
            self.edgeList = keys['edgeList']
        else:
            raise AttributeError("missing attribut")

    def getAdjencyMatrix(self):
        """Function that compute the adjency matrix"""
        adjencyMatrix = []

        # Fill a empty matrix with False
        adjencyMatrix = [False] * self.verticeNumber
        for i in range(self.verticeNumber):
            adjencyMatrix[i] = [False] * self.verticeNumber

        # Assign value to the matrix
        for edge in self.edgeList:
            adjencyMatrix[edge[0]][edge[1]] = True

        return adjencyMatrix

    def getValueMatrix(self):
        """Function that compute the values matrix"""
        valueMatrix = []

        # Fill a empty matrix with None value
        valueMatrix = [None] * self.verticeNumber
        for i in range(self.verticeNumber):
            valueMatrix[i] = [None] * self.verticeNumber

        # Assign value to the matrix
        for edge in self.edgeList:
            valueMatrix[edge[0]][edge[1]] = edge[2]

        return valueMatrix

    def hasCicle(self) -> bool:
        adjencyMatrix = self.getAdjencyMatrix()
        verticeList = list(range(self.verticeNumber))
        finish = False
        while (len(verticeList) != 0 and not finish):
            removed = 0
            for vertice in verticeList:
                if (hasPredecessor(vertice, adjencyMatrix)):
                    verticeList.remove(vertice)
                    del adjencyMatrix[vertice]
                    removed += 1
            if(not removed):
                finish = True

        if (len(verticeList) == 0):
            return False
        else:
            return True

    def __str__(self):
        """Function that display a graph"""
        verticeNumberStr = str(self.verticeNumber) + " vertices\n"
        edgeNumberStr = str(self.edgeNumber) + " edges\n"
        edgeListStr = ""
        for edge in self.edgeList:
            edgeListStr += str(edge[0]) + " -> " + \
                str(edge[1]) + " = " + str(edge[2]) + "\n"
        return verticeNumberStr + edgeNumberStr + edgeListStr
