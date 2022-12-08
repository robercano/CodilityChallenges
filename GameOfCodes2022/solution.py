class Block:
    def __init__(self, size, letter):
        self.size = size
        self.letter = letter


def get_basic_blocks(S):
    allBlock = []

    currentLetter = ''
    currentBlock = None

    # Collapse trivial blocks
    for i in range(len(S)):
        if S[i] == currentLetter:
            currentBlock.size += 1
        else:
            currentBlock = Block(1, S[i])
            allBlock.append(currentBlock)
            currentLetter = S[i]

    return allBlock

def solution(S: str) -> int:
    allBlock = get_basic_blocks(S)

    letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    lastBlock = {k: [None, None, None, None] for k in letters}
    lastBlockLength = {k: [0, 0, 0, 0] for k in letters}

    maxLengthBefore = [-1, -1, -1, 0]

    for i in range(len(allBlock)):
        b = allBlock[i]

        for j in range(4):
            if maxLengthBefore[j] == -1:
                continue

            currentMax = maxLengthBefore[j]

            # combine from last
            if lastBlock[b.letter][j] != None:
                combineLength = lastBlockLength[b.letter][j] + b.size
                
                maxLengthBefore[j] = max(currentMax, combineLength)
                
                lastBlock[b.letter][j] = b
                lastBlockLength[b.letter][j] = combineLength

            if j > 0: # stay
                combineLength = currentMax + b.size
                
                maxLengthBefore[j - 1] = max(maxLengthBefore[j - 1], combineLength)

                lastBlock[b.letter][j - 1] = b
                lastBlockLength[b.letter][j - 1] = max(lastBlockLength[b.letter][j - 1], combineLength)

    return max(maxLengthBefore[0], maxLengthBefore[1], maxLengthBefore[2], maxLengthBefore[3])

TestCases = [['aabacbba', 6],
             ['aabxbaba', 6],
             ['aabxabxba', 6],
             ['xxxyxxyyyxyyy', 11],
             ['atheaxbtheb', 5],
             ['aaaaabaaaa', 10],
             ['qwqertyiuiqoipa', 6],
             ['yyyxxxyxxyyyxyyy', 14],
             ['abcabcabcabc', 6],
             ['abcabcabcabca', 6],
             ['yyyxbzzzxbyyyxbzzzyybyyyxbzzz', 15],
             ['dadadbdacacacbc', 9],
             ['xjojojooojojox', 9],
             ['xjojojooojojo', 9],
             ['zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbabbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 101]]

for test in TestCases:
    result = solution(test[0])
  
    expected = test[1]

    print(test[0] + ' -> ', end='')
    if result == expected:
        print("OK!")
    else:
        print("ERROR! (expected: " + str(expected) + ")" + " (result: " + str(result) + ")")