
def crange(start, end, modulo):
    for i in range(start,end):
        yield i % modulo

def brute_force(A, B):
    N = len(A)
    for i in range(N):
        found = True
        position=0
        for j in crange(N-i, N-i+N, N):
            if A[position] == B[j]:
                found=False
                break
            position+=1
        if found:
            return i

    return -1

def solution(A, B):
    return brute_force(A, B)

TestCases = [[[1,3,5,2,8,7], [7,1,9,8,5,7], 2],
             [[1,1,1,1], [1,2,3,4], -1],
             [[3,5,0,2,4],[1,3,10,6,7], 0]
            ]

for test in TestCases:
    result = solution(test[0], test[1])
    expected = test[2]

    if result == expected:
        print("OK!")
    else:
        print("ERROR! (expected: " + str(expected) + ")" + " (result: " + str(result) + ")")
