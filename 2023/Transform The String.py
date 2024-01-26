tests = int(input())

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for case in range(tests):
    S = input()
    F = input()

    possible = list(F)
    possible_indices = [alphabets.index(x) for x in possible]

    total_transformations = 0


    def find_lowest_transformation(element):
        lowest = 100
        index_of_element = alphabets.index(element)
        for possible_index in possible_indices:
            diff = abs(possible_index - index_of_element)
            if diff > 13:
                diff = 26 - diff
            if lowest > diff:
                lowest = diff
        return lowest


    for letter in S:
        if letter not in possible:
            current_transormations = find_lowest_transformation(letter)
            total_transformations += current_transormations

    print(f"Case #{case+1}: {total_transformations}")
