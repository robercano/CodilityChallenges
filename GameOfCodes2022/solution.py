
import sys, os
import copy

class Node:
    def __init__(self, letter, count, prev, next=None):
        self.letter = letter
        self.count = count
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return '[' + self.letter + ',' + str(self.count) + ']';

class Graph:
    def __init__(self, S):
        self.head = None
        self.tail = None
        self.num_nodes = 0
        self.reversed = False

        self.__build__(S)

    def append(self, letter, count):
        if self.head == None:
            self.head = Node(letter, count, None)
            self.tail = self.head
        else:
            self.tail.next = Node(letter, count, self.tail)
            self.tail = self.tail.next

        self.num_nodes += 1

    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev

        self.num_nodes -= 1

    def removeRange(self, fromNode, toNode):
        node = fromNode
        while node != None and node != toNode:
            nextNode = node.next
            self.remove(node)
            node = nextNode

    def iterFrom(self, node):
        return GraphIterator(self, node)

    def reverse(self):
        self.reversed = not self.reversed

    def __build__(self, S):
        for letter in S:
            if self.tail == None or self.tail.letter != letter:
                self.append(letter, 1)
            else:
                self.tail.count += 1

    def __iter__(self):
        return GraphIterator(self, self.head if not self.reversed else self.tail)

    def __reversed__(self):
        graph = copy.deepcopy(self)
        graph.reversed = not graph.reversed
        return graph

    def __len__(self) -> int:
        return self.num_nodes

    def __str__(self) -> str:
        graph_str = ''
        for node in self:
            graph_str += str(node)
        return graph_str

class GraphIterator:
    def __init__(self, graph, fromNode):
        self.current = fromNode    
        self.reversed = graph.reversed
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            node = self.current
            if self.reversed:
                self.current = self.current.prev
            else:
                self.current = self.current.next
            return node

def reverse(S):
    return S[::-1]

def build_graph(S):
    graph = Graph()

    for letter in S:
        if graph.tail == None or graph.tail.letter != letter:
            graph.append(letter, 1)
        else:
            graph.tail.count += 1

    return graph

def collapse_nodes(graph, fromNode):
    letter_count = {}
    max_group_count = 0
    num_groups_to_remove = 0

    print('graph:' + str(graph))
    print('fromNode: ' + str(fromNode))

    for node in graph.iterFrom(fromNode):
        if node == fromNode:
            continue

        if node.letter == fromNode.letter:
            if node.count < max_group_count or len(graph) - num_groups_to_remove < 3:
                return False

            fromNode.count += node.count
            fromNode.next = node.next

            graph.removeRange(fromNode.next, node)

            return True
        else:
            if node.letter not in letter_count:
                letter_count[node.letter] = node.count
            else:
                letter_count[node.letter] += node.count

            if letter_count[node.letter] > max_group_count:
                max_group_count = letter_count[node.letter]

        if max_group_count > fromNode.count:
            return False

        num_groups_to_remove += 1
    
    return False

def reduce_group(graph, fromNode):
    print('reduce right ' + str(graph))
    while collapse_nodes(graph, fromNode):
        continue
    
    graph.reverse()

    print('reduce left')
    while collapse_nodes(graph, fromNode):
        continue

    graph.reverse()

def reduce_graph(graph):
    exclusion_list = []
    while True:
        if len(graph) <= 3:
            break

        reduced_graph = filter(lambda node: node not in exclusion_list, graph)
        biggest_node = max(reduced_graph, key=lambda node: node.count)

        length_before = len(graph)
        reduce_group(graph, biggest_node)

        if length_before == len(graph):
            exclusion_list.append(biggest_node)
        else:
            exclusion_list = []

def solution(S):
    graph = Graph(S)

    reduce_graph(graph)
    return 0
    print(end='\n')
    sorted_groups = sorted(groups_list, key=lambda x: x.count, reverse=True)
    print('sorted_groups_list: ', end='')
    print_list(sorted_groups)
    print(end='\n')
    first_three_groups = sorted_groups[:3]
    first_three_counts = [group.count for group in first_three_groups]
    
    print_graph(head)

    return sum(first_three_counts), head

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

# TestCases = [['aabacbba', 6],['aabxbaba', 6],
#                  ['xxxyxxyyyxyyy', 11], ['atheaxbtheb', 5],
#                  ['aaaaabaaaa', 10], ['qwqertyiuiqoipa', 6],
#                  ['yyyxxxyxxyyyxyyy', 14], ['abcabcabcabc', 6],
#                  ['abcabcabcabca', 6], ['yyyxbzzzxbyyyxbzzzyybyyyxbzzz', 15],
#                  ['dadadbdacacacbc', 9], ['xjojojooojojox', 9],
#                  ['xjojojooojojo', 9]]
TestCases = [['yyyxbzzzxbyyyxbzzzyybyyyxbzzz', 15]]

for test in TestCases:
 
    #blockPrint()
    print('----------------------')
    print('String: ' + test[0])

    result, head = solution(test[0])

    print('Result: ' + str(result))
    print('Expected: ' + str(test[1]))
    print('----------------------')

    enablePrint()
    
    expected = test[1]

    print(test[0] + ' -> ', end='')
    if result == expected:
        print("OK!")
    else:
        print("ERROR! (expected: " + str(expected) + ")" + " (result: " + str(result) + ")")
        print_graph(head)
        break

