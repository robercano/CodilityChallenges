# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

Tests = [
    [[4, 0, 2, -2], [4, 1, 2, -3], ["R", "G", "R", "R"], 2],
    [[1, 1, -1, 1], [1, -1, 1, -1], ["R", "G", "R", "G"], 4],
    [[1, 0, 0], [0, 1, -1], ["G", "G", "R"], 0],
    [[5, -5, 5], [1, -1, -3], ["G", "R", "G"], 2],
    [[3000, -3000, 4100, -4100, -3000], [5000, -5000, 4100, -4100, 5000], ["R", "R", "G", "R", "G"], 2],
]

import math

def vector_length(X, Y):
    return math.sqrt(X**2 + Y**2)

def solution(X, Y, colors):

    if len(X) == 0 or len(Y) == 0:
        return 0
    
    points = list(zip(X, Y, colors))
    
    reds_distances = [vector_length(point[0], point[1]) for point in points if point[2] == "R"]
    greens_distances = [vector_length(point[0], point[1]) for point in points if point[2] == "G"]

    reds_distances.sort()
    greens_distances.sort()

    minimum_length = min(len(reds_distances), len(greens_distances))

    total_pairs = minimum_length * 2

    for i in reversed(range(minimum_length)):
        # If there is one more element on the reds
        if (len(reds_distances) > i+1 and greens_distances[i] >= reds_distances[i+1]):
            total_pairs -= 2
            continue
        
        # If there is one more element on the greens
        if (len(greens_distances) > i+1 and reds_distances[i] >= greens_distances[i+1]):
            total_pairs -= 2
            continue

        break

    return total_pairs

for test in Tests:
    calculatedSolution = solution(test[0], test[1], test[2])
    expectedSolution = test[3]

    if (calculatedSolution == expectedSolution):
        print("Test passed")
    else:
        print("Test failed")