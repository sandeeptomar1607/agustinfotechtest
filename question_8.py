# Given an array of integers representing the numbers on squares of a chocolate bar, and
# two integers, d (the desired sum) and m (the length of the segment), find the number of
# ways the bar can be divided. A division is valid if a contiguous
# segment of the bar of length m sums to d [Mark 2]
# For example,
# Input: s = [2, 2, 1, 3, 2], d = 4, m = 2 Expected
# Output:
# An integer representing the number of valid ways to divide the bar. For the example
# input, the segments of length 2 are:
# [2,2] -> sum = 4 (Match) [2,1] -
# > sum = 3
# [1,3] -> sum = 4 (Match)
# [3,2] -> sum = 5


def birthday(s,d,m):
    count = 0

    window_sum = su(s[:m])
    
    if window_sum == d:
        count+= 1
    
    for i in range(m, len(s)):
        window_sum += s[i]
        window_sum -= s[i-m]

        if window_sum == d:
            count += 1

    return count

s = [2, 2, 1, 3, 2]
d = 4
m = 2

result = birthday(s, d, m)

print(result)