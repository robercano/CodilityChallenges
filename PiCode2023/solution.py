def solution(P, Q):
    letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    letterSelectedCount = {k: [0, {ik: 0 for ik in letters}] for k in letters}
    stringLength = len(P)

    for i in range(stringLength):
        if P[i] != Q[i]:
            letterSelectedCount[P[i]][0] += 1
            letterSelectedCount[P[i]][1][Q[i]] -= 1

            letterSelectedCount[Q[i]][0] += 1
            letterSelectedCount[Q[i]][1][P[i]] -= 1
        else:
            letterSelectedCount[P[i]][0] += 1

    letterSelectedCount = dict(sorted(letterSelectedCount.items(), key=lambda item: item[1][0]))

    print(letterSelectedCount)

    currentCount = 0
    lettersCount = 0

    while True:
        item = letterSelectedCount.popitem()       
        count = item[1]
        currentCount += count[0]
        lettersCount += 1

        for (letter, discount) in count[1].items():
            if (letter in letterSelectedCount):
                letterSelectedCount[letter][0] += discount

        if currentCount >= stringLength:
            break

        letterSelectedCount = dict(sorted(letterSelectedCount.items(), key=lambda item: item[1][0]))
        print("----------------------------")
        print(letterSelectedCount)

    return lettersCount

TestCases = [
             [ "axxz", "yzwy", 2 ],
            #  [ "ad", "bc", 2 ],
            #  [ "abc", "bcd", 2 ],
            #  [ "bacad", "abada", 1 ],
            #  [ "amz", "amz", 3 ]
            ]

for test in TestCases:
    result = solution(test[0], test[1])
    expected = test[2]

    if result == expected:
        print("OK!")
    else:
        print("ERROR! (expected: " + str(expected) + ")" + " (result: " + str(result) + ")")
