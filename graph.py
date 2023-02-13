graph = { 0 : [1, 8],
          1 : [0, 2, 9],
          2 : [1, 3, 10],
          3 : [2, 4, 11],
          4 : [3, 5, 12],
          5 : [4, 6, 13],
          6 : [5, 14, 7],
          7 : [6],
          8 : [0, 9, 15],
          9 : [1, 8, 10, 16],
          10 : [2, 9, 11, 17],
          11 : [3, 10, 12, 18],
          12 : [4, 11, 13, 19],
          13 : [5, 12, 14, 20],
          14 : [6, 13],
          15 : [8, 16, 21],
          16 : [9, 15, 17, 22],
          17 : [10, 16, 18, 23],
          18 : [11, 17, 19, 24],
          19 : [12, 18, 20, 25],
          20 : [13, 19],
          21 : [15, 22, 26],
          22 : [16, 21, 23, 27],
          23 : [17, 22, 24, 28],
          24 : [18, 23, 25, 29],
          25 : [19, 24],
          26 : [21, 27, 30],
          27 : [22, 26, 28, 31],
          28 : [23, 27, 29, 32],
          29 : [24, 28],
          30 : [26, 31, 33],
          31 : [27, 32, 34],
          32 : [28, 31],
          33 : [30, 34, 35],
          34 : [31, 33],
          35 : [33],
        }

visitedList = [[]]

def depthFirst(graph, currentNode, visited):
    visited.append(currentNode)
    for vertex in graph[currentNode]:
        if len(visited) != 8:
            depthFirst(graph, vertex, visited.copy())
    if len(visited) == 8:
        visitedList.append(visited)

depthFirst(graph, 0, [])

print(len(visitedList))
# print(visitedList)