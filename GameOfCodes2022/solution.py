import sys, os
import copy

class Node:
    def __init__(self, letter, count, id, prev, next=None):
        self.letter = letter
        self.count = count
        self.prev = prev
        self.next = next
        self.id = id

    def __str__(self) -> str:
        return '[' + str(self.id) + ',' + self.letter + ',' + str(self.count) + ']';

    def __eq__(self, other) -> bool:
        return other != None and self.id == other.id

class Graph:
    def __init__(self, S):
        self.head = None
        self.tail = None
        self.num_nodes = 0
        self.reversed = False
        self.id_counter = 0

        self.__build__(S)

    def append(self, letter, count):
        self.id_counter += 1

        if self.head == None:
            self.head = Node(letter, count, self.id_counter, None)
            self.tail = self.head
        else:
            self.tail.next = Node(letter, count, self.id_counter, self.tail)
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

    def removeRange(self, fromNode, toNode, excludeFrom=False, excludeTo=False):
        iter = self.iterFrom(fromNode)
        if excludeFrom:
            next(iter)

        for node in iter:
            if node == toNode:
                if excludeTo == False:
                    self.remove(node)
                break
                
            self.remove(node)

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

    print('      [COLLAPSE NODES]')
    print('        g: ' + str(graph))
    print('        n: ' + str(fromNode))

    for node in graph.iterFrom(fromNode):
        if node == fromNode:
            continue

        if node.letter == fromNode.letter:
            if node.count < max_group_count or len(graph) - num_groups_to_remove < 3:
                return False

            print('        removeRange(' + str(fromNode) + ',' + str(node) + ')')

            fromNode.count += node.count

            graph.removeRange(fromNode, node, excludeFrom=True)

            print('        graph after remove:' + str(graph))

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

def collapse_one_node(graph, fromNode):
    print('  [COLLAPSE]')
    print('    g: ' + str(graph))
    print('    n: ' + str(fromNode))
    print('    [REDUCE RIGHT]')
    while collapse_nodes(graph, fromNode):
        continue
    
    graph.reverse()

    print('    [REDUCE LEFT]')
    while collapse_nodes(graph, fromNode):
        continue

    graph.reverse()

def find_max_node(graph, exclusion_list):
    reduced_graph = filter(lambda node: node not in exclusion_list, graph)
    try:
        return max(reduced_graph, key=lambda node: node.count)
    except ValueError:
        return None

def reduce_graph(graph):
    exclusion_list = []
    while True:
        if len(graph) <= 3:
            break

        max_node = find_max_node(graph, exclusion_list)
        if max_node == None:
            break
        
        length_before = len(graph)
        collapse_one_node(graph, max_node)
        length_after = len(graph)

        if length_before == length_after:
            exclusion_list.append(max_node)
        else:
            exclusion_list = []

def solution(S):
    graph = Graph(S)

    reduce_graph(graph)

    sorted_groups = sorted(list(graph), key=lambda x: x.count, reverse=True)
    first_three_groups = sorted_groups[:3]
    first_three_counts = [group.count for group in first_three_groups]
    
    return sum(first_three_counts), graph

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

TestCases = [['aabacbba', 6],['aabxbaba', 6],
                 ['xxxyxxyyyxyyy', 11], ['atheaxbtheb', 5],
                 ['aaaaabaaaa', 10], ['qwqertyiuiqoipa', 6],
                 ['yyyxxxyxxyyyxyyy', 14], ['abcabcabcabc', 6],
                 ['abcabcabcabca', 6], ['yyyxbzzzxbyyyxbzzzyybyyyxbzzz', 15],
                 ['dadadbdacacacbc', 9], ['xjojojooojojox', 9],
                 ['xjojojooojojo', 9]]
#TestCases = [['yyyxbzzzxbyyyxbzzzyybyyyxbzzz', 15]]

for test in TestCases:
 
    blockPrint()
    print('----------------------')
    print('String: ' + test[0])

    result, graph = solution(test[0])

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
        break

