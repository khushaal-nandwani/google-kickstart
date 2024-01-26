# UTC first two digits * 3600 + last two digits  = seconds
first_greater_than_second = False
# if sign is same => add
# else subtract
addition = False

# STEP 1: find total utc difference
input = "Sun 10 May 2015 13:54:36 -0700"
input_2 = 'Fri 01 May 2015 13:54:36 -0000'
# Day dd Mon yyyy hh:mm:ss +xxxx
# 012345678901234567890123456789
utc_difference = 0

first = int(input[26:28]) * 60 + int(input[28:30])
second = int(input_2[26:28]) * 60 + int(input_2[28:30])
if input[25] != '+':
    first = - first

if input_2[25] != '+':
    second = - second

utc_difference = first + second

# STEP 2: Find datewise difference
year_diff = abs(input[11:])

# STEP3: Subtract the datewise difference from utc difference





