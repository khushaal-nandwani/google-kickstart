#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

# def get_highest_ranked(ranked: List) -> int:
#     hr = 1
#     previousScore = ranked[0]
    
#     for score in ranked[1:]:
#         if score == previousScore:
#             continue
#         previousScore = score
#         hr += 1
    
#     return hr

def climbingLeaderboard(ranked: List, player):
    ranked.insert(0, max(player) + 100)
    newRanked = list(set(ranked))
    newRanked.sort(reverse=True)
    ranks = []
    reversed_ranked = newRanked[::-1]
    # delete repeated elements
    

    player_popper = player[::-1]

    #  get the first score
    curr_score = player_popper.pop()

    hr = len(newRanked)
    # start the loop from end
    for i in range(len(newRanked)):
        elm = reversed_ranked[i]

        if curr_score == elm:
            ranks.append(hr - 1)
            if not player_popper:
                return ranks
            curr_score = player_popper.pop()

        # if score is smaller than elm
        while curr_score < elm:
            ranks.append(hr)
            # get the next score and check again
            if not player_popper:
                return ranks
            curr_score = player_popper.pop()

        hr -= 1
    
    return ranks



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # ranked_count = int(input().strip())

    # ranked = list(map(int, input().rstrip().split()))

    # player_count = int(input().strip())

    # player = list(map(int, input().rstrip().split()))

    # ranked = [997, 981, 957, 933, 930, 927, 926, 920, 916, 896, 887, 874, 863, 863, 858, 847, 815, 809, 803, 794, 789, 785, 783, 778, 764, 755, 751, 740, 737, 730, 691, 677, 652, 650, 587, 585, 583, 568, 546, 541, 540, 538, 531, 527, 506, 493, 457, 435, 430, 427, 422, 422, 414, 404, 400, 394, 387, 384, 374, 371, 369, 369, 368, 365, 363, 337, 336, 328, 325, 316, 314, 306, 282, 277, 230, 227, 212, 199, 179, 173, 171, 168, 136, 125, 124, 95, 92, 88, 85, 70, 68, 61, 60, 59, 44, 43, 28, 23, 13, 12]
    # ranked = [100, 100, 50, 40, 40, 20, 10]
    # player = [50, 65, 77, 90, 102]
    ranked = [13, 12]
    player = [12]
    # player = [12, 20, 30, 32, 35, 37, 63, 72, 83, 85, 96, 98, 98, 118, 122, 125, 129, 132, 140, 144, 150, 164, 184, 191, 194, 198, 200, 220, 228, 229, 229, 236, 238, 246, 259, 271, 276, 281, 283, 287, 300, 302, 306, 307, 312, 318, 321, 325, 341, 341, 341, 344, 349, 351, 354, 356, 366, 369, 370, 379, 380, 380, 396, 405, 408, 417, 423, 429, 433, 435, 438, 441, 442, 444, 445, 445, 452, 453, 465, 466, 467, 468, 469, 471, 475, 482, 489, 491, 492, 493, 498, 500, 501, 504, 506, 508, 523, 529, 530, 539, 543, 551, 552, 556, 568, 569, 571, 587, 591, 601, 602, 606, 607, 612, 614, 619, 620, 623, 625, 625, 627, 638, 645, 653, 661, 662, 669, 670, 676, 684, 689, 690, 709, 709, 710, 716, 724, 726, 730, 731, 733, 737, 744, 744, 747, 757, 764, 765, 765, 772, 773, 774, 777, 787, 794, 796, 797, 802, 805, 811, 814, 819, 819, 829, 830, 841, 842, 847, 857, 857, 859, 860, 866, 872, 879, 882, 895, 900, 900, 903, 905, 915, 918, 918, 922, 925, 927, 928, 929, 931, 934, 937, 955, 960, 966, 974, 982, 988, 996, 996]
    # player = [5, 25, 50, 120]

    result = climbingLeaderboard(ranked, player)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
