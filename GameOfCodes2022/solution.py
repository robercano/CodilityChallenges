# Based on siakhooi solution

def solution(S: str) -> int:
    letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    blockLength = {k: [0, 0, 0] for k in letters}
    maxLength = [-1, -1, -1]

    for letter in S:
        cachedMaxLength = maxLength.copy()

        for j in range(0, 3):
            combineLength = blockLength[letter][j] + 1
            appendLength = cachedMaxLength[j-1] + 1 if j > 0 else 1

            maxLength[j] = max(maxLength[j], combineLength, appendLength)
            blockLength[letter][j] = max(blockLength[letter][j], combineLength, appendLength)
        
    return max(maxLength)

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