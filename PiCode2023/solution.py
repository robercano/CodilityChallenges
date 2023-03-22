import sys
import os

import copy

class Group:
    def __init__(self, letterA, letterB, count):
        self.letters = { letterA: letterB, letterB: letterA }
        self.count = count

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __str__(self):
        return str(self.letters) + " -> " + str(self.count)
    
    def __repr__(self):
        return str(self.letters) + " -> " + str(self.count)

def solution(P, Q):
    orig_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')

    groups = [ Group(P[0], Q[0], 1) ]

    for i in range(1, len(P)):
        letterP = P[i]
        letterQ = Q[i]

        newGroups = []

        print("All new groups start", groups)

        for group in groups:
            print("Group!!!!", group)
            print("Letters: ", letterP, ",", letterQ )

            isPInGroup = letterP in group.letters
            isQInGroup = letterQ in group.letters

            if isPInGroup and isQInGroup and group.letters[letterP] == letterQ and group.letters[letterQ] == letterP:
                print("=== Same group, same letters")
                continue

            if not isPInGroup and not isQInGroup:
                print("=== Same group, new letters")
                if letterP != letterQ:
                    group.letters[letterP] = letterQ
                    group.letters[letterQ] = letterP
                else:
                    group.letters[letterP] = None

                group.count += 1
            elif isPInGroup:
                print("=== New group with P letter")

                newGroup = copy.deepcopy(group)

                otherLetter = group.letters[letterP]
                group.letters[letterP] = None

                if otherLetter is not None:
                    del group.letters[otherLetter]

                del newGroup.letters[letterP]
                if otherLetter is not None:
                    newGroup.letters[otherLetter] = None
                newGroup.letters[letterQ] = None
                newGroup.count += 1

                newGroups.append(newGroup)

                print("New group", newGroup)
            elif isQInGroup:
                print("=== New group with Q letter")

                newGroup = copy.deepcopy(group)

                otherLetter = group.letters[letterQ]
                group.letters[letterQ] = None

                if otherLetter is not None:
                    del group.letters[otherLetter]

                del newGroup.letters[letterQ]
                if otherLetter is not None:
                    newGroup.letters[otherLetter] = None
                newGroup.letters[letterP] = None
                newGroup.count += 1

                newGroups.append(newGroup)

                print("New group", newGroup)
        
        print("All new groups", newGroups)
        if len(newGroups) > 0:
            groups.extend(newGroups)

    sys.stdout = orig_stdout

    return min(groups, key = lambda group: group.count).count

TestCases = [
             ['adabca', 'cbdcdb', 3],
             [ "axxz", "yzwy", 2 ],
             [ "ad", "bc", 2 ],
             [ "abc", "bcd", 2 ],
             [ "bacad", "abada", 1 ],
             [ "amz", "amz", 3 ],
             [ "aaadb", "bbbce", 2 ],
             ['dddabc', 'abcefg', 3], 
             ['bsqafgiulewghfiaaplskfhjkldsafjhlkafgsdjhluhefdiuahfulidhg', 
              'bsdafgiulewghficahlskfhjklzfafjhlkafgsdjwluhefdiurhfueidhg', 14] 
            ]

for test in TestCases:
    result = solution(test[0], test[1])
    expected = test[2]

    if result == expected:
        print("OK!")
    else:
        print("ERROR! (expected: " + str(expected) + ")" + " (result: " + str(result) + ")")
