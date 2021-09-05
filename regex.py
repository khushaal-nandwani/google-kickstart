import re

s = input()
sub_s = input()


def string_finder(sq, sub_sq):
    all_mats = []

    match = re.search(sub_sq, sq)

    if match is None:
        print('(-1, -1)')
    else:
        all_mats.append((match.start(), match.end()-1))
        x = match.start() + 1
        while match.start() != -1:
            # trim the strings
            new_match = re.search(sub_s, s[x:])
            if new_match is None:
                break
            if new_match.start() != -1:
                all_mats.append((new_match.start() + x, new_match.end() + x - 1))
                x += new_match.start() + 1


    for mat in all_mats:
        print(f'({mat[0]}, {mat[1]})')


string_finder(s, sub_s)
