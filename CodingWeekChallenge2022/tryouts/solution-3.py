def matrix_zero(n, m):
    return [[0 for col in range(n)] for row in range(m)]

def matrix_true(n, m):
    return [[True for col in range(n)] for row in range(m)]

def matrix_multiply(A, B):
    return [[sum([x*y for (x, y) in zip(row, col)]) for col in zip(*B)] for row in A]

def matrix_sum(matrix):
    return sum([sum(row) for row in matrix])

def matrix_print(matrix):
    print("[", end="")
    for i in range(len(matrix)):
        row = matrix[i]
        if i == len(matrix) - 1:
            print(" " + str(row), end="]\n")
        elif i == 0:
            print(str(row), end=",\n")
        else:
            print(" " + str(row), end=",\n")

def matrix_mask(matrix, mask):
    return [[matrix[row][col] if mask[row][col] else 0 for col in range(len(matrix[row]))] for row in range(len(matrix))]

def mask_from_matrix(matrix, prev_mask):
    return [[True if matrix[row][col] == 0 and prev_mask[row][col] else False for col in range(len(matrix[row]))] for row in range(len(matrix))]

def get_adjacency_matrix(A, B):
    adjacency_matrix = matrix_zero(len(A) + 1, len(A) + 1)
    
    for i in range(len(A)):
        node_index_A = A[i]
        node_index_B = B[i]

        adjacency_matrix[node_index_A][node_index_B] = 1
        adjacency_matrix[node_index_B][node_index_A] = 1

    return adjacency_matrix

def solution(A, B):
    if len(A) != len(B):
        return 0

    if len(A) == 0:
        return 0

    if(len(A) == 1):
        return 1
    
    if (len(A) == 2):
        return 2
        
    adjacency_matrix = get_adjacency_matrix(A, B)
    adjacency_matrix_squared = matrix_multiply(adjacency_matrix, adjacency_matrix)
    
    mask = matrix_true(len(A) + 1, len(A) + 1)
    num_paths = 0

    while True:
        adjacency_matrix = matrix_mask(adjacency_matrix, mask)

        num_new_paths = matrix_sum(adjacency_matrix)
        if num_new_paths == 0:
            break

        mask = mask_from_matrix(adjacency_matrix, mask)

        num_paths += num_new_paths
        adjacency_matrix = matrix_multiply(adjacency_matrix, adjacency_matrix_squared)

    return num_paths // 2

if __name__ == "__main__":
    Tests = [
        [[0, 3, 4, 2, 6, 3], [3, 1, 3, 3, 3, 5], 6],
        [[0, 4, 2, 2, 4], [1, 3, 1, 3, 5], 9],
        [[0, 4, 4, 2, 7, 6, 3], [3, 5, 1, 3, 4, 3, 4], 16],
    ]

    for test in Tests:
        result = solution(test[0], test[1])

        if (result == test[2]):
            print("Test passed")
        else:
            print("Test failed")
            print("Expected: ", test[2])
            print("Actual: ", result)