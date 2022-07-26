'''
input format: a graph is input as an adjacency matrix of the following form:
input = [ 
  [0, 8, 5, 0, 0, 0, 0], 
  [8, 0, 10, 2, 18, 0, 0], 
  [5, 10, 0, 3, 0, 16, 0], 
  [0, 2, 3, 0, 12, 30, 14], 
  [0, 18, 0, 12, 0, 0, 4], 
  [0, 0, 16, 30, 0, 0, 26], 
  [0, 0, 0, 14, 4, 26, 0] 
] 

The rows and columns of the matrix represent all the possible vertices.
Values to the left of the diagonal represent the 

Output: a list of tuples, wherein each tuple represents an edge of the MST as (v1, v2, 
weight) 
'''

def Prims(G:list)->list:
    #store the number of vertices in the graph
    vertices = len(G)
    # here the index represents the vertex, the number stored represents the node that has been visited 
    visited = [0]
    result = []
    #start a loop to go through all of the nodes until each has been visited
    while len(visited) < vertices:
        #set an arbitrarily high number to begin the comparison at the start of each loop
        minimum = 999999
        # loop through each visited node and check its edges for the least value
        for i in visited:
            #check all values in the row relative to 
            for j in range(len(G[i])):
                # if j is not 0 (which represents no edge), j is less than the previous minimum and has not been visited before
                if G[i][j] and G[i][j] < minimum and j not in visited:
                    minimum = G[i][j]
                    new_edge = [i, j, G[i][j]]
        visited.append(new_edge[1])
        result.append(tuple(new_edge.copy()))

    return result

if __name__ == '__main__':
    G = [[0, 9, 75, 0, 0],
         [9, 0, 95, 19, 42],
         [75, 95, 0, 51, 66],
         [0, 19, 51, 0, 31],
         [0, 42, 66, 31, 0]]

    print(Prims(G))
