def solution(tiles):
    total_rotations = {}
    fixed_rotations = [1,2,1,0]
    
    for tile in tiles:
        new_rotations = {}

        for letter_index in range(0,len(tile)):
            letter = tile[letter_index]
            new_letter = tile[(letter_index + 2) % 4]

            previous_rotations = total_rotations[letter] if letter in total_rotations else 0

            new_rotations[new_letter] = previous_rotations + fixed_rotations[letter_index]

        total_rotations = new_rotations

    return min(total_rotations.values())

TestCases = [[["RGBW", "GBRW"], 1],
             [["WBGR", "WBGR", "WRGB", "WRGB", "RBGW"], 4],
             [["RBGW", "GBRW", "RWGB", "GBRW"], 2],
             [["GBRW", "RBGW", "BWGR", "BRGW"], 2]
             ]

for test in TestCases:
 
    result = solution(test[0])
    expected = test[1]

    if result == expected:
        print("OK!")
    else:
        print("ERROR! (expected: " + str(expected) + ")" + " (result: " + str(result) + ")")
