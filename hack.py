def solve(s: str):
    possible = False
    output = ''
    if s[0].isalpha():
        output += s[0].title()
    else:
        output += s[0]
    # iterate through the string
    for i in range(1, len(s)):
        if s[i] == ' ':
            possible = True
            output += s[i]
            continue
        if possible and s[i].isalpha():
            output += s[i].title()
            possible = False
            continue
        possible = False
        output += s[i]
    return output


print(solve('1 w 2 r 3g'))
