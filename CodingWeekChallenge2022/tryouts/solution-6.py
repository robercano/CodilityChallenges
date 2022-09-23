
def newAdjacencyList(N):
    return [[] for x in range(N)]

def newFrequencies(N):
    return [0 for x in range(N)]

# Structure of a Node
class Node:
    def __init__(self, v, label):
        self.node = v
        self.edgeLabel = label

numEdges = 0
numNodes = 0
adj = None
freq = None
maxFrequency = 0

# Function to perform DFS
def dfs(u = 1, p = 1):
    global numNodes
    global maxFrequency
    global adj
    global freq

    # Add the current node to
    # size of subtree rooted at u
    sz = 1
     
    # Iterate over its children
    for a in adj[u]:
         
        # Check if child is not parent
        if a.node != p:
             
            # Get the subtree size
            # for the child
            val = dfs(a.node, u)
             
            frequency = val * (numNodes - val)

            # Set the frequency
            # of the current edge
            freq[a.edgeLabel] = frequency

            if frequency > maxFrequency:
                maxFrequency = frequency
             
            # Add the subtree size
            # to itself
            sz += val
             
    # Return the subtree size
    return sz

def calculate_frequencies(A, B):
    global numEdges
    global numNodes
    global maxFrequency
    global adj
    global freq

    numEdges = len(A)
    numNodes = len(A) + 1
    maxFrequency = 0
    
    # Create an adjacency list
    adj = newAdjacencyList(numNodes)

    # Create an array to store
    # the frequency of each edge
    freq = newFrequencies(numEdges)

    # Add edges to the graph
    for i in range(len(A)):
        addEdge(adj, A[i], B[i], i)

    dfs()

def addEdge(adj, u, v, label):
    adj[u].append(Node(v, label))
    adj[v].append(Node(u, label))
       
def solution(A, B):
    calculate_frequencies(A, B)
    return maxFrequency
     
if __name__ == "__main__":
    Tests = [
        # [[0, 3, 4, 2, 6, 3], [3, 1, 3, 3, 3, 5], 6],
        # [[0, 4, 2, 2, 4], [1, 3, 1, 3, 5], 9],
        # [[0, 4, 4, 2, 7, 6, 3], [3, 5, 1, 3, 4, 3, 4], 16],
        # [[1, 2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 0], 7],
        # [[1, 2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 1], 12],
        # [[1, 2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 2, 1], 15],
        # [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0], 8],
        # [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 0, 1], 14],
        # [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 2, 1], 18],
        # [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 3, 2, 1], 20],
        # [[1, 2, 3, 4, 5], [0, 0, 0, 1, 4], 8],
        [[0, 0, 0, 0, 0, 6, 7, 8, 7], [1, 2, 3, 4, 5, 5, 5, 5, 9], 24],
        [[0, 0, 0, 0, 5, 6, 7, 8, 7], [1, 2, 3, 4, 4, 4, 4, 4, 9], 25]
    ]

    for test in Tests:
        result = solution(test[0], test[1])

        if (result == test[2]):
            print("[Test passed]\n")
        else:
            print("[Test failed]")
            print("  Input:", test[0], test[1])
            print("  Frequencies:", freq)
            print("  Expected: ", test[2])
            print("  Actual: ", result)
            print()