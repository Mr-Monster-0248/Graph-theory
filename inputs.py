"""
All inputs functions of the project
"""


def readGraphFromFile(filename: str):
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

    return verticeNumber, edgeNumber, edgeList


def getFilePathFromGraphNumber():
    graphNumber = input("Enter the graph number: ")
    return "./graphs/graph{}.txt".format(graphNumber)


if (__name__ == "__main__"):
    readGraphFromFile("./graphs/graph1.txt")
