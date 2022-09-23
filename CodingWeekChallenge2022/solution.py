class Node:
    def __init__(self):
        self.nexts = []
        self.parity = 0
        self.visited = False

def createGraph(A, B):
    nodes = [Node() for i in range(len(A) + 1)]

    isPureStar = True
    possibleStar = None

    for i in range(len(A)):
        if len(nodes[A[i]].nexts) >= 1:
            if possibleStar != None:
                if possibleStar != A[i]:
                    isPureStar = False
            else:
                possibleStar = A[i]

        if len(nodes[B[i]].nexts) >= 1:
            if possibleStar != None:
                if possibleStar != B[i]:
                    isPureStar = False
            else:
                possibleStar = B[i]

        nodes[A[i]].nexts.append(nodes[B[i]])
        nodes[B[i]].nexts.append(nodes[A[i]])
    
    return nodes, isPureStar

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
        
    nodes, isPureStar = createGraph(A, B)

    if isPureStar:
        return len(nodes) - 1;

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
