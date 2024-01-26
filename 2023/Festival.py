import bisect

def insert(lister, n):
    # Searching for the position
    for i in range(len(lister)):
        if lister[i] > n:
            index = i
            break

    # Inserting n in the list
    lister = lister[:i] + [n] + lister[i:]
    return lister

def total_of_day(special_string):
    values = special_string.split('%')
    total = 0
    for x in values:
        total += int(x)
    return total

def convert_each_to_int(given_list):
    for i in range(len(given_list)):
        given_list[i] = int(given_list[i])

cases = int(input())
for test in range(cases):

    details = input().split()
    D = int(details[0])     # the total days
    N = int(details[1])     # total attractions
    K = int(details[2])     # attractions you can attend in a day
    placeholder_string = '0' + '%0' * (K - 1)
    happiness = [placeholder_string for i in range(D)]      # list of strings

    for i in range(N):
        event_details = input().split()
        start_day = int(event_details[1])
        end_day = int(event_details[2])
        h_value = int(event_details[0])
        index = start_day - 1
        for index in range(start_day, end_day + 1):
            day_info = happiness[index - 1]
            values_in_target = day_info.split('%')
            convert_each_to_int(values_in_target)
            # there are K values
            if h_value < int(values_in_target[0]):
                continue
            else:
                print(values_in_target, 'this si the original')
                values_in_target = insert(values_in_target, h_value)
                print(values_in_target, 'this is inserted')
                values_in_target = values_in_target[1:]
                original_form = f'{values_in_target[0]}'
                for i in range(1, K ):
                    # print(i, values_in_target)
                    original_form += f'%{values_in_target[i]}'
                happiness[index - 1] = original_form
    print(happiness)
    max = 0
    for i in range(D):
        total = total_of_day(happiness[i])
        if total > max:
            max = total

    print(f'Case #{test + 1}: {max}')

