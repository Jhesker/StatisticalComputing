# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 21:12:50 2019

@author: jhesk
"""
class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')'\
            + self.dest.getName()
class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                + dest.getName() + '\n'
        return result[:-1]
class Graph(Digraph):
    def addEdge(self, edge):
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
def printPath(path):
    result =''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
            #print the edge value somewhere aroung here
    return result
def DFS(graph, start, end, path, shortest, toPrint = False):
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
    return shortest
def shortestPath(graph, start, end, toPrint = False):
    return DFS(graph, start, end, [], None, toPrint)

def BFS(graph, start, end, toPrint = False):
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS path:', printPath(path))
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
def test():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    w1 = WeightedEdge(Edge(nodes[0],nodes[1]), 1)
    w2 = WeightedEdge(nodes[1],nodes[2], 3)
    w3 = WeightedEdge(nodes[2],nodes[3], 4)
    w4 = WeightedEdge(nodes[2],nodes[4], 1)
    w5 = WeightedEdge(nodes[3],nodes[4], 2)
    w6 = WeightedEdge(nodes[3],nodes[5], 5)
    w7 = WeightedEdge(nodes[0],nodes[2], 1)
    w8 = WeightedEdge(nodes[1],nodes[0], 1)
    w9 = WeightedEdge(nodes[3],nodes[1], 4)
    w10 = WeightedEdge(nodes[4],nodes[0], 2)
    w11 = WeightedEdge(nodes[2],nodes[5], 14)
    g.addEdge(w1)
    g.addEdge(w2)
    g.addEdge(w3)
    g.addEdge(w4)
    g.addEdge(w5)
    g.addEdge(w6)
    g.addEdge(w7)
    g.addEdge(w8)
    g.addEdge(w9)
    g.addEdge(w10)
    g.addEdge(w11)
    sp = shortestPath(g, nodes[0], nodes[5], toPrint = True)
    print('Shortest path is', printPath(sp))
    sp = BFS(g, nodes[0], nodes[5])
    print('Shortest path found by BFS:', printPath(sp))
test()

