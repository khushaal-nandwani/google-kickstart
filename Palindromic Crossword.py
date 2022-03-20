cases = int(input())

def change(row_number: int, col_number: int, crossword: list, exceptions: list):
    dots_eliminated = 0
    letters_added = []

    row_result = False
    col_result = False

    if (row_number, col_number) not in exceptions and crossword[row_number][col_number].isalpha():
        letter = crossword[row_number][col_number]

        copy = crossword[row_number]
        end_hash = cols
        hash_index = col_number
        if end_hash > col_number:
            try:
                end_hash = copy.index('#', hash_index + 1, -1)
                hash_index = end_hash
            except ValueError:
                pass

        copy_2 = crossword[row_number][:col_number]
        copy_2.reverse()
        try:
            start_hash = copy_2.index('#') + 1
        except ValueError:
            start_hash = len(copy_2) + 1

        # changing in the row
        if crossword[row_number][end_hash - start_hash] == '.':
            dots_eliminated += 1
            crossword[row_number][end_hash - start_hash] = letter
            letters_added.append((row_number, col_number))
            row_result = True
            exceptions.append((row_number, col_number))

        elements = []
        for i in range(rows):
            elements.append(crossword[i][col_number])
        end_hash = rows
        hash_index = row_number
        if end_hash > row_number:
            try:
                end_hash = elements.index('#', hash_index + 1, -1)
                hash_index = end_hash
            except ValueError:
                pass
        copy_2 = elements[:row_number]
        copy_2.reverse()
        try:
            start_hash = copy_2.index('#') + 1
        except ValueError:
            start_hash = len(copy_2) + 1

        # changing in the column
        if crossword[end_hash - start_hash][col_number] == '.':
            dots_eliminated += 1
            crossword[end_hash - start_hash][col_number] = letter
            letters_added.append((row_number, col_number))
            col_result = True
            exceptions.append((row_number, col_number))

    count_and_letters = [dots_eliminated] + letters_added
    return (col_result or row_result, count_and_letters)

for test in range(cases):
    r_n_c = input()
    r_n_c = r_n_c.split()
    rows = int(r_n_c[0])
    cols = int(r_n_c[1])

    inital_dots = 0
    crossword = []
    for row in range(rows):
        get_row = list(input())
        dots = get_row.count('.')
        crossword.append(get_row)

    exceptions = []
    dots_eliminated = 0

    for row_number in range(rows):
        for col_number in range(cols):
            changed = change(row_number, col_number, crossword, exceptions)
            if changed[0]:
                # we did change some letter
                info = changed[1]
                count = info[0]
                dots_eliminated += count
                for index in range(count):
                    active = True
                    while active:
                        changed_inner = change(info[index + 1][0], info[index + 1][1], crossword, exceptions)
                        if not changed_inner[0]:
                            active = False
                            break




            # (
            # True/False,
            # if True -> [count, (row_number, col_number), .... ]
            # )

            # if (row_number, col_number) not in exceptions and crossword[row_number][col_number].isalpha():
            #     letter = crossword[row_number][col_number]
            #
            #     copy = crossword[row_number]
            #     end_hash = cols
            #     hash_index = col_number
            #     if end_hash > col_number:
            #         try:
            #             end_hash = copy.index('#', hash_index + 1, -1)
            #             hash_index = end_hash
            #         except ValueError:
            #             pass
            #     copy_2 = crossword[row_number][:col_number]
            #     copy_2.reverse()
            #     try:
            #         start_hash = copy_2.index('#') + 1
            #     except ValueError:
            #         start_hash = len(copy_2) + 1
            #
            #     # changing in the row
            #     if crossword[row_number][end_hash - start_hash] == '.':
            #         dots_eliminated += 1
            #         crossword[row_number][end_hash - start_hash] = letter
            #         # check for letter
            #
            #     elements = []
            #     for i in range(rows):
            #         elements.append(crossword[i][col_number])
            #     end_hash = rows
            #     hash_index = row_number
            #     if end_hash > row_number:
            #         try:
            #             end_hash = elements.index('#', hash_index + 1, -1)
            #             hash_index = end_hash
            #         except ValueError:
            #             pass
            #     copy_2 = elements[:row_number]
            #     copy_2.reverse()
            #     try:
            #         start_hash = copy_2.index('#') + 1
            #     except ValueError:
            #         start_hash = len(copy_2) + 1
            #
            #     # changing in the column
            #     if crossword[end_hash - start_hash][col_number] == '.':
            #         dots_eliminated += 1
            #         crossword[end_hash - start_hash][col_number] = letter

                # exceptions.append((row_number, col_number))

    printed_crossword = ''
    for row in crossword:
        for element in row:
            printed_crossword += element
        printed_crossword += '\n'

    printed_crossword = printed_crossword[:-1]


    print(f'Case #{test + 1}: {dots_eliminated}\n{printed_crossword}')





