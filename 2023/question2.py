#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'shortestTransferDistance' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts INTEGER_ARRAY c as parameter.
#

def shortestTransferDistance(c):
    # c = [0, 1, 2, 3, 4, 5, 6, 7]
    var_x = c[4] - c[0]
    con_x = c[5] - c[1]
    var_y = c[2] - c[6]
    con_y = c[3] - c[7]

    x_sign = same_signs(var_x, con_x)
    y_sign = same_signs(var_y, con_y)
    print(x_sign, y_sign)
    # consider the case of t getting cacncelled out
    if x_sign and y_sign:
        return math.sqrt(con_x^2 + con_y^2)
    else:
        if x_sign and not y_sign:
            return abs(con_x)
        if y_sign and not x_sign:
            return abs(con_y)
        else:
            return 0


def same_signs(a, b) -> bool:
    if a > 0 and b > 0:
        return True
    if a < 0 and b < 0:
        return True
    return False



if __name__ == '__main__':
    print(shortestTransferDistance([-2, -1, 1, 1, 1, 1, -2, -1]))
