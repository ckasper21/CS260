#!/usr/bin/env python2
#   floyd.py (HW8)
#   Author: Chris Kasper
#   Date: 3/2/18
#

import sys
INF = 1000000

def ConstructGraph(f_name):
    f = open(f_name, "r")
    
    line = f.readline()
    count = 0
    while line:
        count += 1
        line = f.readline()    

    f.seek(0)
    G = [[INF for i in range(count)] for j in range(count)]

    for v in range(0,len(G)):
        G[v][v] = 0

    line = f.readline()
    idx = 0
    while line:
        line_split = line.split()
        for i in range(1,len(line_split)):
                if i == idx:
                    G[i][idx] = 0
                pair_split = line_split[i].split(",")
                G[idx][int(pair_split[0])] = int(pair_split[1])
                G[int(pair_split[0])][idx] = int(pair_split[1])
        idx += 1 
        line = f.readline()

    return G

def floydw(graph):
    num_vert = len(graph)
    dist = [[INF for i in range(num_vert)] for j in range(num_vert)]
    pred = [[-1 for i in range(num_vert)] for j in range(num_vert)]
    
    for i in range(0,num_vert):
        for j in range(0,num_vert):
            if (graph[i][j] != INF) and (graph[i][j] != 0):
                dist[i][j] = graph[i][j]
                pred[i][j] = i
            else:
                dist[i][j] = INF
                pred[i][j] = -1
            if i == j:
                dist[i][j] = 0
                pred[i][j] = -1

    for k in range(0,num_vert):
        for i in range(0,num_vert):
            for j in range(0,num_vert):
                if (dist[i][k] + dist[k][j]) < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    print("\nHere is the dist matrix")
    PrintMatrix(dist)
    print("\nHere is the pred matrix")
    PrintMatrix(pred)

def PrintMatrix(m):
    for line in m:
        for element in line:
            if element == INF:
                print("INF "),
            else:
                print ("%3d " % element),
        print 





def main():
    # Main Function
    try:
        f_name = sys.argv[1]
    except IndexError:
        print("No input given!")
        sys.exit(0)
   
    G = ConstructGraph(f_name)

    print("Here is the graph")
    PrintMatrix(G)

    floydw(G)

if __name__ == '__main__':
    main()
