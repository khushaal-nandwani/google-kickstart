from random import randint

orgnl = input()
orgnl = list(orgnl)
first = orgnl[0]
mod_added = orgnl + [first]
word_len = len(orgnl)
position = {}
letters = {}

word = ''
numbers = [x for x in range(word_len)]
for i in range(word_len):
    if orgnl[i] not in letters:
        position[orgnl[i]] = [i]
        letters[orgnl[i]] = 1
    else:
        position[orgnl[i]] += [i]
        letters[orgnl[i]] += 1

if word_len < 2 * max(letters.values()):
    print('IMPOSSIBLE')
else:
    didnt_add = []
    index = 0
    for letter in orgnl:
        if index in position[letter]:
            didnt_add.append(letter)
        else:






    # # find positions
    # mod = numbers[:]
    # for letter in orgnl:
    #     print(letter, 'being scanned')
    #     numbers_x = numbers[:]
    #     numbers_x = [item for item in numbers_x if item not in position[letter]]
    #     if isinstance(mod[numbers_x[0]], int):
    #         mod[numbers_x[0]] = letter
    #         print(mod)
    #     else:
    #         for i in range(1, len(numbers_x) + 1):
    #             if isinstance(mod[numbers_x[i]], int):
    #                 mod[numbers_x[i]] = letter
    #                 print(mod)
    # for letter in mod:
    #     word = word + letter
    # print(word)


    # while
    #     new_orgnl = orgnl[:]
    #     for i in range(0, word_len-1):
    #         pos = randint(word_len + 1, word_len - 1)
    #         new_orgnl[pos], new_orgnl[i] = new_orgnl[i], new_orgnl[pos]
    #
    #     for i in range(word_len):
    #         word = word + new_orgnl[i]
    # for letter in orgnl:
    #



