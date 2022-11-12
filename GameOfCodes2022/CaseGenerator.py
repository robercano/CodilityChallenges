def string_to_count(S):
    SC = [[S[0], 1]]
    letters = {}
    letters[S[0]] = 1
    max_letter = 1

    for elem in S[1:]:
        if elem == SC[-1][0]:
            SC[-1][1] += 1
            letters[elem] += 1
            if letters[elem] > max_letter:
                max_letter = letters[elem]
        else:
            SC.append([elem, 1])
            if elem in letters:
                letters[elem] += 1
                if letters[elem] > max_letter:
                    max_letter = letters[elem]
            else:
                letters[elem] = 1

    # print(S, SC, letters, max_letter)

    return SC, max_letter


def solution_loop(SC, count_max, remining_length):
    options = {}
    options[(())] = 0
    options[tuple(tuple(SC[0]))] = SC[0][1]
    # print(options)
    remining_length -= SC[0][1]
    # print(remining_length)

    # print(SC)
    for elem in SC[1:]:
        # print("*** Nuevo elem: ", elem)
        remining_length -= elem[1]

        new_options = options.copy()
        # Option 1: Do not add element

        # Option 2: Add element
        # Only add element if we can still get better answer
        for option in options.keys():
            # print(option)
            if option == ():
                option_mod = tuple(elem)
                leng_mod = elem[1]
            else:
                if elem[0] == option[-2]:
                    option_mod = option[:-2] + \
                        (option[-2], (option[-1] + elem[1]))
                    leng_mod = options[option] + elem[1]

                else:
                    # Only keep new letter if total blocks is less than 3
                    if len(option) <= 4:
                        option_mod = option + tuple(elem)
                        leng_mod = options[option] + elem[1]
                    else:
                        continue

            if leng_mod + remining_length > count_max:
                new_options[option_mod] = leng_mod
                if leng_mod > count_max:
                    count_max = leng_mod

            # print(new_options)
        options = new_options
        # print(options)

    return count_max


def solution(S):
    SC, len_min = string_to_count(S)
    count_max = solution_loop(SC, count_max=len_min, remining_length=len(S))
    return count_max


Test_examples = [['aabacbba', 6], ['aabxbaba', 6],
                 ['xxxyxxyyyxyyy', 11], ['atheaxbtheb', 5],
                 ['aaaaabaaaa', 10], ['qwqertyiuiqoipa', 6],
                 ['yyyxxxyxxyyyxyyy', 14], ['abcabcabcabc', 6],
                 ['abcabcabcabca', 6], ['yyyxbzzzxbyyyxbzzzyybyyyxbzzz', 15],
                 ['dadadbdacacacbc', 9], ['xjojojooojojox', 9],
                 ['xjojojooojojo', 9]]

# word = 'aabaaa'
# Test_examples = [[word, solution(word)]]

# word = 'aabaaa'
# Test_examples = [[word, 6]]

word = 'ababababababbabababababababbabababababacacacacacaccacacaca' + \
    'cacacaccacacacacacababababababbabababababababbababababab'
print(solution(word))
SC, max_letter = string_to_count(word)
print(max_letter)

# for example in Test_examples:
#     result = solution(example[0])
#     expected = example[1]
#     if result == expected:
#         print("OK!: ", end='')
#     else:
#         print("ERROR!: ", end='')
#     print(f"Result: {result}, expected: {expected}")
