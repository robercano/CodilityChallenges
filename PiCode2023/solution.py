import sys
import os

memo = {}

def getKey(letter, P, Q):
    return str(letter) + P + Q

def countLetters(letter, P, Q):
    key = getKey(letter, P, Q)
    if key in memo:
        return memo[key]

    if len(P) == 0:
        return [ set([letter]) ]

    letterP = P[0]
    letterQ = Q[0]

    groupsP = countLetters(letterP, P[1:], Q[1:])
    groupsQ = countLetters(letterQ, P[1:], Q[1:])

    groupsP.extend(groupsQ)

    for group in groupsP:
        if letter not in group:
            group.add(letter)
    
    # memo[key] = groupsP
    return groupsP

def solution(P, Q):
    orig_stdout = sys.stdout
    # sys.stdout = open(os.devnull, 'w')

    groupsP = countLetters(P[0], P[1:], Q[1:])
    groupsQ = countLetters(Q[0], P[1:], Q[1:])
 
    groupsP.extend(groupsQ)

    sys.stdout = orig_stdout

    return len(min(groupsP, key = lambda group: len(group)))

TestCases = [
             ['adabca', 'cbdcdb', 3],
            #  [ "axxz", "yzwy", 2 ],
            #  [ "ad", "bc", 2 ],
            #  [ "abc", "bcd", 2 ],
            #  [ "bacad", "abada", 1 ],
            #  [ "amz", "amz", 3 ],
            #  [ "aaadb", "bbbce", 2 ],
            #  ['dddabc', 'abcefg', 3], 
            #  ['bsqafgiulewghfiaaplskfhjkldsafjhlkafgsdjhluhefdiuahfulidhg', 
            #   'bsdafgiulewghficahlskfhjklzfafjhlkafgsdjwluhefdiurhfueidhg', 14] 
            ]

for test in TestCases:
    result = solution(test[0], test[1])
    expected = test[2]

    if result == expected:
        print("OK!")
    else:
        print("ERROR! (expected: " + str(expected) + ")" + " (result: " + str(result) + ")")
