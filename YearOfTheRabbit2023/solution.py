def solution(A, B):
    for i in range(len(A)):
        if not [True for a,b in zip(A,B) if a == b]:
            return i
        B = [B[-1]] + B[0:-1]
    return -1


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
