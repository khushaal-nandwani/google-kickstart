cases = int(input())
for test in range(cases):
    N = int(input())
    S = input()
    bin_locations = []
    bins = []
    index = 0

    for char in S:
        if char == '1':
            bin_locations.append(index)
        #TODO: may remove this bins given_list
        bins.append(char)
        index += 1

    def get_closest_bin(given_list, n, length):
        indi = 0
        while given_list[indi] < n:
            indi += 1
            if indi == length - 1:
                break

        first = abs(n - given_list[indi])
        if length >= 2:
            second = abs(abs(given_list[indi - 1] - n))
            if first > second:
                return second
            else:
                return first
        return first


    sum = 0
    no_of_bins = len(bin_locations)
    for ind in range(N):
        house = bins[ind]
        if house == '1':
            continue
        else:
            closest_bin_index_distance = get_closest_bin(bin_locations, ind, no_of_bins)
            sum += closest_bin_index_distance

    print(f'Case #{test + 1}: {sum}')













