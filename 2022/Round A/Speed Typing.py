test_case = int(input())

for test in range(test_case):
    I = input()
    P = input()

    equal = False
    possible = False

    i = 0
    p = 0
    count = 0

    p_len = len(P)
    i_len = len(I)


    def check_if_equal(letter1, letter2):
        if letter1 == letter2:
            return True
        return False


    def remaining_chars(current_pos, length):
        return length - current_pos - 1


    while p <= p_len - 1:
        i_letter = I[i]
        p_letter = P[p]
        equal = check_if_equal(i_letter, p_letter)
        if equal:
            if i == (i_len - 1):    # last letter of I
                possible = True
                # add the remaining chars in P and return
                remain = remaining_chars(p, p_len)
                count += remain
                break
            else:
                i += 1
                p += 1
        else:
            p += 1
            # since they are not equal we must delete them
            count += 1

    if not possible:
        print(f"Case #{test + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{test + 1}: {count}")
