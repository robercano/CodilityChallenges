class Node:
    def __init__(self):
        self.nexts = []
        self.parity = 0
        self.visited = False

def updateEvenOdd(currentNode, previousNode, new_odd, new_even):
    if new_odd == 0 and new_even == 0:
        return
        
    currentNode.num_connected_odd += new_odd
    currentNode.num_connected_even += new_even

    for next in currentNode.nexts:
        if (next != previousNode):
            updateEvenOdd(next, currentNode, new_even, new_odd)

def printNodes(nodes):
    print ("Graph Degrees:")
    for node in nodes:
        print(len(node.nexts))

def createGraph(A, B):
    nodes = [Node() for i in range(len(A) + 1)]

    for i in range(len(A)):
        nodes[A[i]].nexts.append(nodes[B[i]])
        nodes[B[i]].nexts.append(nodes[A[i]])
    
    return nodes

def findNodeWithGrade(nodes, grade):
    for node in nodes:
        if len(node.nexts) == grade:
            return node

    return None

def bfs(node):
    queue = []
    
    totalOdd = 0
    queue.append(node)

    while queue:
        node = queue.pop(0)

        for next in node.nexts:
            if next.visited:
                continue

            next.parity = 1 - node.parity
            next.visited = True
            queue.append(next)

            if next.parity == 1:
                totalOdd += 1

    return totalOdd

def calculateTotalOdd(node):
    return bfs(node)

def solution(A, B):
    if len(A) != len(B):
        return 0

    if len(A) == 0:
        return 0

    if(len(A) == 1):
        return 1
    
    if (len(A) == 2):
        return 2
        
    nodes = createGraph(A, B)

    root = findNodeWithGrade(nodes, 1)

    totalOdd = calculateTotalOdd(root)

    return (len(nodes) - totalOdd)*totalOdd
    
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
