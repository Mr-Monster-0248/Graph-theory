from input import readGraphFromFile


class Graph:
    """
    Class of a graph, defined by:
    - vertice number
    - edge number
    - list of all the eged with there values as
        [in, out, edge value]
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

    def __str__(self):
        """Function that display a graph"""
        verticeNumberStr = str(self.verticeNumber) + " vertices\n"
        edgeNumberStr = str(self.edgeNumber) + " edges\n"
        edgeListStr = ""
        for edge in self.edgeList:
            edgeListStr += str(edge[0]) + " -> " + \
                str(edge[1]) + " = " + str(edge[2]) + "\n"
        return verticeNumberStr + edgeNumberStr + edgeListStr
