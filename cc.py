# encoding=utf-8
#compute Clustering Coefficient for undirecte graph
import time
from collections import defaultdict

cc_list = []  #store Clustering Coefficient for every node
edge_set = set()  #store adjacent edges

class Graph:
    def __init__(self):
        self.Graph = defaultdict(set)
        self.NodesNum = 0
        self.graphEdge = []

    def Link(self,filename,separator):
        with open(filename,'r',encoding='utf-8') as graphline:
            for line in graphline:
                nodeA,nodeB = line.strip().split(separator)
                self.Graph[nodeA].add(nodeB)
                self.Graph[nodeB].add(nodeA)

                spiltList = line.replace('\n', "").split(" ", 1)
                self.graphEdge.append(spiltList)
            self.NodesNum = len(self.Graph)

    def ClusteringCoefficient(self):
        #compute Clustering Coefficient for average node
        for node in self.Graph:
            self.getCC(node)

    def getCC(self,node):
        for edge in self.graphEdge:
            if edge[0] in self.Graph[node] and edge[1] in self.Graph[node]:
                s = edge[0]+edge[1]
                edge_set.add(s)

        neighbourEdgeNum = len(edge_set)
        neighbourNodeNum = len(self.Graph[node])

        print(node)
        print("neighbour node Num:", neighbourNodeNum)
        print("neighbour edge Num:", neighbourEdgeNum)

        #compute Clustering Coefficient
        ccNum = 0
        if neighbourNodeNum > 1:
            ccNum = 2 * neighbourEdgeNum / ((neighbourNodeNum - 1) * neighbourNodeNum)  # undirecte graph need * 2,but directe graph don't need
        cc_list.append(ccNum)
        edge_set.clear()

    #Average Clustering Coefficient
    def getAverageCC(self):
        sum = 0
        for s in cc_list:
            sum += s
        return sum / len(cc_list)
def main():
    separator = ' '
    filename = 'facebook_combined.txt'
    begin = time.time()
    myGraph = Graph()
    myGraph.Link(filename,separator)
    myGraph.ClusteringCoefficient()
    print("Clustering Coefficient of nodes:",cc_list)
    print("Average Clustering Coefficient:",myGraph.getAverageCC())
    print("Time：",time.time()-begin,'second')

if __name__ == "__main__":
    main()