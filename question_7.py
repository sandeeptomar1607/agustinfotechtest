# Given an unsorted array of integers, you need to write a program to find the length of
# the longest consecutive elements sequence. 


def longest_consecutive(nums):
    numbers = set(nums)

    longest = 0

    for num in numbers:
        if num - 1 not in numbers:
            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))