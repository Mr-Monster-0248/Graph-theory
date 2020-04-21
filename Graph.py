from graphUtils import *
from copy import deepcopy


class Graph:
    """
    Class of a graph, defined by:
    - vertice number
    - edge number
    - list of all the edges with there values as
        [in, out, value]
    - adjency matrix
    - value matrix
    """

    def __init__(self, verticeNumber, edgeNumber, edgeList) -> object:
        """Constructor of Graph class"""
        self.verticeNumber = verticeNumber
        self.edgeNumber = edgeNumber
        self.edgeList = edgeList
        self.verticeList = self._setVerticeList()
        self.adjencyMatrix = self._setAdjencyMatrix()
        self.valueMatrix = self._setValueMatrix()

    @classmethod
    def fromFile(cls, filename) -> object:
        """Function to read graph from specified file"""

        with open(filename, 'r') as myfile:
            lines = myfile.readlines()

        verticeNumber = int(lines[0])
        edgeNumber = int(lines[1])

        edgeList = []
        for i in range(2, edgeNumber + 2):
            line = lines[i].replace('\n', '').split(" ")
            inEdge = int(line[0])
            outEdge = int(line[1])
            value = int(line[2])
            edgeList.append([inEdge, outEdge, value])

        return cls(verticeNumber, edgeNumber, edgeList)

    # ======== Getters =========
    def getAdjencyMatrix(self) -> list:
        return deepcopy(self.adjencyMatrix)

    def getValueMatrix(self) -> list:
        return deepcopy(self.valueMatrix)

    def getVerticeList(self) -> list:
        return deepcopy(self.verticeList)

    # ======== Setters =========
    def _setAdjencyMatrix(self) -> list:
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

    def _setValueMatrix(self) -> list:
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

    def _setVerticeList(self) -> list:
        return list(range(self.verticeNumber))

    # ========= Methods =========
    def hasCicle(self) -> bool:
        """Function that check if the graph has a cicle"""

        print("Using the method of elimination of entry points")
        adjencyMatrix = self.getAdjencyMatrix()
        verticeList = self.getVerticeList()
        finish = False
        while (len(verticeList) != 0 and not finish):
            entryPointList = []
            print("List of vertice before removing entry point " +
                  str(verticeList))

            # Finding entry points
            for index in range(len(verticeList)):
                if (not hasPredecessor(index, adjencyMatrix)):
                    entryPointList.append(index)

            # If no entry point found we stop the search
            if(len(entryPointList) == 0):
                print("No more removable entry point")
                finish = True
            else:
                # Removing entry points
                adjencyMatrix, verticeList = removeEntryPointFromMatrix(
                    entryPointList, adjencyMatrix, verticeList)

        print("Remaining vertices: " + str(verticeList))
        if (len(verticeList) == 0):
            return False
        else:
            return True

    def getRanks(self) -> list:
        print("Using the method of elimination of entry points")
        verticeList = self.getVerticeList()
        currentRank = 0
        ranks = [0] * self.verticeNumber
        adjencyMatrix = self.getAdjencyMatrix()
        while (len(verticeList) != 0):
            print("current rank: " + str(currentRank))
            print("List of vertice before removing entry point " +
                  str(verticeList))
            entryPointList = []

            # Finding entry points
            for index in range(len(verticeList)):
                if (not hasPredecessor(index, adjencyMatrix)):
                    entryPointList.append(index)

            for index in entryPointList:
                ranks[verticeList[index]] = currentRank

            # Removing entry points
            adjencyMatrix, verticeList = removeEntryPointFromMatrix(
                entryPointList, adjencyMatrix, verticeList)

            currentRank += 1

        return ranks

    def isScheduling(self, ranks: list) -> bool:
        """Check if a graph is a scheduling graph"""
        valueMatrix = self.getValueMatrix()
        if (getEntryPointNumber(ranks) > 1):
            print("There is more than one entry point")
            return False
        else:
            print("There is one entry point")

        if (getEndPointNumber(ranks) > 1):
            print("There is more than one exit point")
            return False
        else:
            print("There is one exit point")

        if (hasNegativeEdge(valueMatrix)):
            print("There is a negative edge")
            return False
        else:
            print("There is no negative edge")

        if (not hasSameValueEdges(0, ranks.index(0), valueMatrix)):
            print("There is a non negative outgoing edge from an entry point")
            return False
        else:
            print("There is no non negative outgoing edge from an entry point")

        if (not hasSameWeight(valueMatrix)):
            print("Some vertices have some outgoing edges with different weight")
            return False
        else:
            print("Every vertices have outgoing edges whith the same weight")
            return True

    def __str__(self) -> str:
        """Function that display a graph"""
        verticeNumberStr = str(self.verticeNumber) + " vertices\n"
        edgeNumberStr = str(self.edgeNumber) + " edges\n"
        edgeListStr = ""
        for edge in self.edgeList:
            edgeListStr += str(edge[0]) + " -> " + \
                str(edge[1]) + " = " + str(edge[2]) + "\n"
        return verticeNumberStr + edgeNumberStr + edgeListStr
