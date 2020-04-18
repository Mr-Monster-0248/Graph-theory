"""
Thibault LEPEZ, Matthieu GEDEON, Daniil ROSSO
L3 int - G2
"""
from Graph import Graph
from inputs import getFilePathFromGraphNumber
from outputs import printMatrix

start = True

while(start):
    filepath = getFilePathFromGraphNumber()

    print("* Reading graph from " + filepath)
    graph = Graph(filename=filepath)

    print(graph)

    print("* adjustement matrix")
    adjencyMatrix = graph.getAdjencyMatrix()
    printMatrix(adjencyMatrix)

    print("* values matrix")
    valueMatrix = graph.getValueMatrix()
    printMatrix(valueMatrix)

    print("* Detecting cicles")
    if (graph.hasCicle()):
        print('The graph has a cicle')
    else:
        print("The graph has no cicle")

    choice = input("Start again with another graph? [y/n]: ")
    start = (choice == 'y' or choice == 'Y')
