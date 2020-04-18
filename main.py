"""
Thibault LEPEZ, Matthieu GEDEON, Daniil ROSSO
L3 int - G2
"""
from Graph import *
from inputs import getFilePathFromGraphNumber
from outputs import printMatrix

start = True

while(start):
    filepath = getFilePathFromGraphNumber()

    print("[i] Reading graph from " + filepath)
    graph = Graph(filename=filepath)

    print(graph)

    print("[i] adjustement matrix")
    adjencyMatrix = graph.getAdjencyMatrix()
    printMatrix(adjencyMatrix)

    print("[i] values matrix")
    valueMatrix = graph.getValueMatrix()
    printMatrix(valueMatrix)

    choice = input("Start again with another graph? [y/n]: ")
    start = (choice == 'y' or choice == 'Y')
