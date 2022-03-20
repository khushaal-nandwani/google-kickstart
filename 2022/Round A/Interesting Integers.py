# code from stackoverflow
def sum_digits3(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

# code from geeksforgeeks
def getProduct(n):
    product = 1

    while (n != 0):
        product = product * (n % 10)
        n = n // 10

    return product

test_case = int(input())

for test in range(test_case):
    string = input()
    string = string.split()
    A = int(string[0])
    B = int(string[1])


    count = 0

    for num in range(A, B + 1):
        prod = getProduct(num)
        summ = sum_digits3(num)
        if prod % summ == 0:
            count += 1

    print(f"Case #{test + 1}: {count}")






