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

    print("# Reading graph from " + filepath)
    graph = Graph(filename=filepath)

    print(graph)

    print("# Adjency matrix")
    adjencyMatrix = graph.getAdjencyMatrix()
    printMatrix(adjencyMatrix)

    print("# Values matrix")
    valueMatrix = graph.getValueMatrix()
    printMatrix(valueMatrix)

    print("# Detecting cicles")
    if (graph.hasCicle()):
        print('The graph has a cicle\n')
    else:
        print("The graph has no cicle\n")

        print("# Finging the ranks")
        ranks = graph.getRanks()
        print("The ranks are \t\t" + str(ranks))
        print("For following vertices \t" +
              str(list(range(graph.verticeNumber))))

    choice = input("\nStart again with another graph? [y/n]: ")
    start = (choice == 'y' or choice == 'Y')
