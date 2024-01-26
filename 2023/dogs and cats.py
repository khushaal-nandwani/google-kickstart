test_cases = int(input())

for test in range(test_cases):

    n_d_c_m = input()
    ndcm_list = n_d_c_m.split()
    N = int(ndcm_list[0])
    D = int(ndcm_list[1])
    C = int(ndcm_list[2])
    M = int(ndcm_list[3])

    order = input()
    length = len(order)

    decision = 'YES'

    for i in range(length):
        if order[i] == 'D':
            if D > 0:
                D -= 1
                C += M
            else:
                decision = 'NO'
                break
        elif order[i] == 'C':
            if C > 0:
                C -= 1
            else:
                # check if there are any dogs remaining at the end
                for j in range(i, length):
                    if order[j] == 'D':
                        decision = 'NO'
                        break
    print(f"Case #{test + 1}: {decision}")

