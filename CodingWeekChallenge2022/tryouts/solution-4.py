class Node:
    def __init__(self):
        self.nexts = []

    def __str__(self) -> str:
        return str(self.id)
    def __repr__(self) -> str:
        return str(self.id)

def get_chain_length(node, previous):
    length = 1
    is_end = False

    while is_end == False:
        is_end = True
        for next in node.nexts:
            if next == previous:
                continue

            length += 1
            previous = node
            node = next
            is_end = False

    return length

def get_stars(nodes):
    stars = []
    for node in nodes:
        if len(node.nexts) > 2:
            stars.append(node)

    return stars

def get_star_arms_lengths(star):
    lengths = []
    for node in star.nexts:
        chain_length = get_chain_length(node, star)
        if chain_length > 1:
            lengths.append(chain_length)
    return lengths

def calculate_stars_substracted_paths(nodes):

    stars = get_stars(nodes)

    if len(stars) != 1:
        return 0

    star = stars[0]
    num_nodes = len(nodes)
    arms_length = get_star_arms_lengths(star)
    
    num_arms = len(arms_length)

    if num_nodes % 2 == 0:
        max_arms = num_nodes // 2 - 1
        missing_arms = max_arms - num_arms
        return missing_arms * missing_arms
    else:
        max_arms = (num_nodes - 1) // 2 - 1
        missing_arms = max_arms - num_arms
        return missing_arms * (missing_arms + 1)
    
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

        nodeA.nexts.append(nodeB)
        nodeB.nexts.append(nodeA)

    substracted_paths = calculate_stars_substracted_paths(nodes)

    num_nodes = len(nodes)
    if num_nodes % 2 == 0:
        return (num_nodes * num_nodes // 4) - substracted_paths
    else:
        return (((num_nodes * num_nodes) - 1) // 4) - substracted_paths

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

