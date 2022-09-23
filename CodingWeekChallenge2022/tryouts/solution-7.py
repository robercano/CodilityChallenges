# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from functools import reduce

class Node:
    def __init__(self):
        self.nexts = []
        self.num_connected_odd = 0
        self.num_connected_even = 0

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

def solution(A, B):
    if len(A) != len(B):
        return 0

    if len(A) == 0:
        return 0

    if(len(A) == 1):
        return 1
    
    if (len(A) == 2):
        return 2
        
    nodes = [Node() for i in range(len(A) + 1)]

    for i in range(len(A)):
        nodeA = nodes[A[i]]
        nodeB = nodes[B[i]]

        cacheNumConnectedOdd = nodeA.num_connected_odd
        cacheNumConnectedEven = nodeA.num_connected_even

        updateEvenOdd(nodeA, None, nodeB.num_connected_even + 1, nodeB.num_connected_odd)
        updateEvenOdd(nodeB, None, cacheNumConnectedEven + 1, cacheNumConnectedOdd)

        nodes[A[i]].nexts.append(nodes[B[i]])
        nodes[B[i]].nexts.append(nodes[A[i]])

    printNodes(nodes)
        
    return reduce(lambda x, y: x + y, [node.num_connected_odd for node in nodes]) // 2

if __name__ == "__main__":
    Tests = [
        # [[0, 3, 4, 2, 6, 3], [3, 1, 3, 3, 3, 5], 6],
        # [[0, 4, 2, 2, 4], [1, 3, 1, 3, 5], 9],
        # [[0, 4, 4, 2, 7, 6, 3], [3, 5, 1, 3, 4, 3, 4], 16],
        # [[0, 0, 1, 1, 2, 2],[1, 2, 3, 4, 5, 6], 12]
        # [[0, 0, 0, 3, 3, 2, 5],[1, 2, 3, 4, 5, 6], 12]
        [[0, 0, 0, 0, 0, 6, 7, 8, 7], [1, 2, 3, 4, 5, 5, 5, 5, 9], 24],
        [[0, 0, 0, 0, 5, 6, 7, 8, 7], [1, 2, 3, 4, 4, 4, 4, 4, 9], 25]
    ]

    for test in Tests:
        result = solution(test[0], test[1])

        if (result == test[2]):
            print("Test passed")
        else:
            print("Test failed")

