from math import floor

class Path:
    def __init__(self, next, head, length):
        self.next = next
        self.head = head
        self.length = length

    def __str__(self) -> str:
        return f'\n------Path--------\n  Next: {self.next.id}\n  Head: {self.head.id}\n  Length: {self.length}\n------------------'
    def __repr__(self) -> str:
        return f'Path(n:{self.next.id}, h:{self.head.id}, l:{self.length})'

class Node:
    def __init__(self, id):
        self.id = id
        self.paths = {}

    def add_path(self, path):
        self.paths[path.head] = path

    def get_path(self, head):
        return self.paths.get(head)

    def get_num_paths(self):
        return len(self.paths)

    def delete_path(self, head):
        return self.paths.pop(head)

    def is_head(self):
        num_paths = self.get_num_paths()
        return num_paths == 1 or num_paths > 2

    def is_single_node(self):
        return self.get_num_paths() == 0

    def is_single_chain_head(self):
        return self.get_num_paths() == 1

    def is_single_chain(self):
        num_paths = self.get_num_paths()
        return num_paths == 1 or num_paths == 2

    def is_multi_chain(self):
        return self.get_num_paths() > 2

    def get_other_head(self) -> Path:
        return list(self.paths.values())[0]

    def __str__(self) -> str:
        return f'\n-------Node-------\n  ID: {self.id}\n  Paths: {self.paths}\n  Paths Length:{self.get_num_paths()}\n  Is Head: {self.is_head()}\n------------------'
    def __repr__(self) -> str:
        return str(self.id)

def calcChainOddConnections(chainLength):
    return floor(chainLength * chainLength / 4)

def find_head(nodes):
    for node in nodes:
        if node.is_head:
            return node

def calculate_paths(current_head_node, previous_head_node):
    num_paths = 0

    print("Current_head_node: ", current_head_node)
    print("Number of head nodes: ", len(current_head_node.head_nodes))
    
    if len(current_head_node.head_nodes) == 0:
        return 0

    for i in range(len(current_head_node.head_nodes)):
        node = current_head_node.head_nodes[i]

        if node != previous_head_node:
            num_paths += current_head_node.chain_lengths[i] + calculate_paths(node, current_head_node)

    return num_paths

def update_single_path(current_node, old_head, new_head, chain_length):
    print("Delete path")
    print(current_node.paths)
    print(old_head)
    print(old_head.head)

    old_path = current_node.delete_path(old_head.head)

    current_node.paths[new_head] = Path(old_path.next, new_head, chain_length)

    if current_node.is_head() == False:
        update_single_path(old_path.next, old_head, new_head, chain_length + 1)

def update_paths(current_node, new_path_node):
    for path in current_node.paths.values():
        if path.next != new_path_node:
            print("Update Paths")
            print(path)

            old_head = current_node.get_other_head()
            update_single_path(path.next, old_head, current_node, 2)

def print_nodes(nodes):
    print("--------------------------------")
    print("              NODES             ")
    print("--------------------------------")
    for node in nodes:
        print(node)
    print("--------------------------------")

def solution(A, B):
    if len(A) != len(B):
        return 0

    if len(A) == 0:
        return 0

    if(len(A) == 1):
        return 1
    
    if (len(A) == 2):
        return 2
        
    nodes = [Node(i) for i in range(len(A) + 1)]

    for i in range(len(A)):
        nodeA = nodes[A[i]]
        nodeB = nodes[B[i]]

        print("--------------------------------")
        print(" Processing edge: ", A[i], B[i])
        print("--------------------------------")
        print(nodeA)
        print(nodeB)

        wasSingleChainNodeA = nodeA.is_single_chain()
        wasSingleChainNodeB = nodeB.is_single_chain()
        wasSingleChainHeadNodeA = nodeA.is_single_chain_head()
        wasSingleChainHeadNodeB = nodeB.is_single_chain_head()

        if wasSingleChainHeadNodeA:
            print("Node A is single chain head")
            # print(nodeA.is_single_chain_head())
            # print(nodeA)

            other_head = nodeA.get_other_head()

            print("Other head")
            print(other_head)
            print("----------")

            nodeB.add_path(Path(nodeA, other_head.head, other_head.length + 1))
        else:
            print("Node A is NOT single chain head")
            nodeB.add_path(Path(nodeA, nodeA, 2))
            
        if wasSingleChainHeadNodeB:
            print("Node B is single chain head")
            # print(nodeB.is_single_chain_head())
            # print(nodeB)

            other_head = nodeB.get_other_head()

            # print("Other head")
            # print(other_head)

            nodeA.add_path(Path(nodeB, other_head.head, other_head.length + 1))
        else:
            print("Node B is NOT single chain head")
            nodeA.add_path(Path(nodeB, nodeB, 2))

        print_nodes(nodes)

        if wasSingleChainNodeA:
            update_paths(nodeA, nodeB)
        if wasSingleChainNodeB:
            update_paths(nodeB, nodeA)

        print_nodes(nodes)

    headNode = find_head(nodes)
    return calculate_paths(headNode, None)

if __name__ == "__main__":
    Tests = [
        [[0, 3, 4, 2, 6, 3], [3, 1, 3, 3, 3, 5], 6]
        #[[0, 4, 2, 2, 4], [1, 3, 1, 3, 5], 9],
        #[[0, 4, 4, 2, 7, 6, 3], [3, 5, 1, 3, 4, 3, 4], 16],
    ]

    for test in Tests:
        result = solution(test[0], test[1])

        if (result == test[2]):
            print("Test passed")
        else:
            print("Test failed")
            print("  Expected: ", test[2])
            print("  Actual: ", result)