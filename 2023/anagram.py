from random import choice
import collections

testcases = int(input())

for j in range(testcases):
    given = input()
    length = len(given)

    x = collections.Counter(given).most_common(1)[0]
    x = x[1]

    if x > length / 2:
        print(f'Case #{j+1}: IMPOSSIBLE')
        continue

    word = list(given)
    # alphabets = given_list(word)
    numbers = [x for x in range(length)]
    orgnl_word = given

    for i in range(length):
        temp = numbers[:]
        active = True
        while active:
            x = choice(temp)
            if word[i] != word[x] and word[x] != orgnl_word[i] and word[i] != orgnl_word[x]:
                word[i], word[x] = word[x], word[i]
                active = False
            else:
                temp.remove(x)
                if temp == []:
                    break
                x = choice(temp)
    word = ''.join(map(str, word))
    print(f'Case #{j+1}:', word)




# for letter in word:
#     if letter not in placements:
#         placements[letter] = [length]
#     else:
#         placements[letter].append(length)
#     length += 1





















#
# alphabets.sort()
#
# final_word = ''
# index = 0
# temp_index = 0
#
#
# for letter in alphabets:
#     placed = False
#     while not placed:
#         # we want to place it
#         # check if the index can be placed
#         if temp_index not in placements[letter]:
#             index += 1
#             temp_index += 1
#             break
#         else:
#             # we were not able to place it in the first attempt
#             temp_index += 1
#     # placing the new placements
#     if letter not in new_placements:
#         new_placements[letter] = [temp_index]
#     else:
#         new_placements[letter].append(temp_index)
#
#     temp_index = index
#
#
