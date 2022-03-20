def get_divisor(number):
    for x in possible_divisors:
        if number % x == 0:
            return x


def first_sober_element(data):
    ind = 0
    try:
        while data[ind] == 1:
            ind += 1
        return ind
    except IndexError:
        return -1


def stroke_everything(divi, canvas, start, end):
    stroke = canvas[start:end]
    for i in range(len(stroke)):
        stroke[i] = int(stroke[i] / divi)
    canvas = canvas[:start] + stroke + canvas[end:]


VALUES = {
    "U": 0,
    "R": 2,
    "Y": 3,
    "B": 5,
    "O": 6,
    "P": 10,
    "G": 15,
    "A": 30
}

possible_divisors = [2, 3, 5]

tests = int(input())

for case in range(tests):
    length = int(input())
    paints = list(input())
    strokes = 0

    element_to_start_with = 0
    paint_values = [VALUES[x] for x in paints]

    while True:
        element_to_start_with = first_sober_element(paint_values)
        if element_to_start_with == -1:
            break
        divisor = get_divisor(paint_values[element_to_start_with])
        copy_paint_values = paint_values[element_to_start_with:]
        for i in range(len(copy_paint_values)):
            element = copy_paint_values[i]
            if element // divisor == element / divisor:
                copy_paint_values[i] = element // divisor
            else:
                break
        paint_values = paint_values[:element_to_start_with] + copy_paint_values
        strokes += 1

    print(f"Case #{case + 1}: {strokes}")

