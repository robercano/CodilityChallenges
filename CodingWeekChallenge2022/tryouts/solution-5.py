# Python program for the above approach
from queue import Queue
 

def newAdjacencyList(N):
    return [[] for x in range(N)]

# Function to add an edge in the tree
def addEdge(adj, a1, a2):
    # print("Adding edge", a1, a2)
    adj[a1].append(a2);
    adj[a2].append(a1);
 
# Function to convert the given tree
# into a bipartite graph using BFS
def toBipartite(adj, N):
    setNum = [-1] * N
 
    # Stores the current node during
    # the BFS traversal of the tree
    q = Queue();
 
    # Initialize the set number of
    # 1st node and enqueue it
    q.put(0);
    setNum[0] = 0;
 
    # BFS traversal of the given tree
    while (not q.empty()):
 
        # Current node
        v = q.queue[0];
        q.get();
 
        # print("Current node: ", v)

        # Traverse over all neighbours
        # of the current node
        for u in adj[v]:
 
            # If the set is not assigned
            if (setNum[u] == -1):
 
                # Assign set number to node u
                # print("  Setting set number for node", u, "to", setNum[v] ^ 1)
                setNum[u] = setNum[v] ^ 1;
                q.put(u);
             
    return setNum

# Function to find if the path length
# between node A and B is even or odd
def isPathOdd(tree, A, B):
    # If the set number of both nodes is
    # same, path length is odd else even
    # print(A, B, tree[A], tree[B])
    return tree[A] != tree[B];

def printBipartiteTree(tree):
    print("Bipartite Tree")
    print("--------------")
    for i in range(0, len(tree)):
        print(i, tree[i])
    print("--------------")

def printAdjacencyList(adj):
    print("Adjacency List")
    print("--------------")
    for i in range(0, len(adj)):
        print(i, adj[i])
    print("--------------")

def solution(A, B):
    N = len(A) + 1;

    adjacencyList = newAdjacencyList(N)
    # printAdjacencyList(adjacencyList)

    for (a, b) in zip(A, B):
        addEdge(adjacencyList, a, b)

    # printAdjacencyList(adjacencyList)
    
    bipartiteTree = toBipartite(adjacencyList, N);

    # printBipartiteTree(bipartiteTree)

    total_odd = 0
    for i in range(0, N):
        for j in range(i + 1, N):
            if isPathOdd(bipartiteTree, i, j):
                total_odd += 1

    return total_odd

if __name__ == "__main__":
    Tests = [
        [[0, 3, 4, 2, 6, 3], [3, 1, 3, 3, 3, 5], 6],
        [[0, 4, 2, 2, 4], [1, 3, 1, 3, 5], 9],
        [[0, 4, 4, 2, 7, 6, 3], [3, 5, 1, 3, 4, 3, 4], 16],
        [[1, 2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 0], 7],
        [[1, 2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 1], 12],
        [[1, 2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 2, 1], 15],
        [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0], 8],
        [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 0, 1], 14],
        [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 2, 1], 18],
        [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 3, 2, 1], 20],
        [[1, 2, 3, 4, 5], [0, 0, 0, 1, 4], 8],
    ]

    for test in Tests:
        result = solution(test[0], test[1])

        if (result == test[2]):
            print("Test passed")
        else:
            print("Test failed")
            print("  Expected: ", test[2])
            print("  Actual: ", result)