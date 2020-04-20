"""
Thibault LEPEZ, Matthieu GEDEON, Daniil ROSSO
L3 int - G2
"""
from Graph import Graph
from graphUtils import printMatrix


start = True

while(start):
    graphNumber = input("Enter the graph number: ")
    filepath = "./graphs/graph{}.txt".format(graphNumber)

    try:
        print("# Reading graph from " + filepath)
        graph = Graph.fromFile(filepath)
    except FileNotFoundError:
        print("[ERROR] File not found")
    else:
        print(graph)

        print("# Adjency matrix")
        printMatrix(graph.getAdjencyMatrix())

        print("# Values matrix")
        printMatrix(graph.getValueMatrix())

        print("# Detecting cicles")
        if (graph.hasCicle()):
            print('The graph has a cicle\n')
        else:
            print("The graph has no cicle\n")

            print("# Finging the ranks")
            ranks = graph.getRanks()
            print("The ranks are \t\t" + str(ranks))
            print("For following vertices \t" + str(graph.getVerticeList()))

            print("\n# Checking if graph is a scheduling graph")
            if (graph.isScheduling(ranks)):
                print("The graph is a scheduling graph")
            else:
                print("The graph is not a scheduling graph")
    finally:
        choice = input("\nStart again with another graph? [y/n]: ")
        start = (choice == 'y' or choice == 'Y')
