from collections import deque
import random


#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()
    

#Define my own
def get_size(self):
    return len(self.adj)

Graph.get_size = get_size

def number_of_nodes(self):
    return len(self.adj)

Graph.number_of_nodes = number_of_nodes
    


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


# BFS3
def BFS3(G, start):
    Q = deque([start])

    isMarked = {start: True}
    for node in G.adj:
        if node != start:
            isMarked[node] = False

    predd = {}

    while len(Q) != 0:
        currNode = Q.popleft()
        for node in G.adj[currNode]:
            if not isMarked[node]:
                isMarked[node] = True
                predd[node] = currNode
                Q.append(node)

    return predd

# DFS3
def DFS3(G, start):
    Q = [start]   # using list as stack for DFS

    isMarked = {start: True}
    for node in G.adj:
        if node != start:
            isMarked[node] = False

    predd = {}

    while len(Q) != 0:
        currNode = Q.pop()   # pop from end (stack behavior)
        for node in G.adj[currNode]:
            if not isMarked[node]:
                isMarked[node] = True
                predd[node] = currNode
                Q.append(node)

    return predd

# BFS2
def BFS2(G, node1, node2):

    predd = BFS3(G, node1)

    if node1 == node2:
        return [node1]

    if node2 not in predd:
        return []

    pathway = []
    currNode = node2

    while currNode != node1:
        pathway.append(currNode)
        currNode = predd[currNode]

    pathway.append(node1)

    pathway.reverse()

    return pathway

# DFS2
def DFS2(G, node1, node2):

    predd = DFS3(G, node1)

    if node1 == node2:
        return [node1]

    if node2 not in predd:
        return []

    pathway = []
    currNode = node2

    while currNode != node1:
        pathway.append(currNode)
        currNode = predd[currNode]

    pathway.append(node1)

    pathway.reverse()

    return pathway

# has_cycle
def has_cycle(G):

    isMarked = {}
    for node in G.adj:
        isMarked[node] = False

    for start in G.adj:

        if not isMarked[start]:

            Q = [(start, None)]
            isMarked[start] = True

            while len(Q) != 0:
                currNode, parentNode = Q.pop()

                for node in G.adj[currNode]:

                    if not isMarked[node]:
                        isMarked[node] = True
                        Q.append((node, currNode))

                    elif node != parentNode:
                        return True

    return False

# is_connected
def is_connected(G):

    if len(G.adj) <= 1:
        return True

    predd = BFS3(G, 0)

    countREACHING = 1 + len(predd)

    return countREACHING == len(G.adj)

# create_random_graph
def create_random_graph(i, j):

    G = Graph(i)

    setsofEDGES = set()

    edgesMAX = i * (i - 1) // 2

    if j > edgesMAX:
        j = edgesMAX

    while len(setsofEDGES) < j:

        n1 = random.randint(0, i - 1)
        n2 = random.randint(0, i - 1)

        if n1 == n2:
            continue

        edge = (min(n1, n2), max(n1, n2))

        if edge not in setsofEDGES:
            setsofEDGES.add(edge)
            G.add_edge(n1, n2)

    return G


#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


