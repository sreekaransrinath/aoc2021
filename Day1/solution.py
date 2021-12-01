# Read Input
with open("Day1/input.txt") as f:
    input = [int(line) for line in f.readlines()]

# Initial Solution

# Part 1
# count = 0
# for i in range(len(input) - 1):
#     if input[i] < input[i + 1]:
#         count += 1

# print(count)

# Part 2
# count = 0
# sliding_window = 3
# for i in range(len(input) - sliding_window):
#     if (
#         input[i] + input[i + 1] + input[i + 2]
#         < input[i + 1] + input[i + 2] + input[i + 3]
#     ):
#         count += 1

# print(count)

# Improved solution
# If you think about it, Part 1 is nothing more than a simpler case of Part 2, with a sliding window size of 1. And comparing sliding windows, in input[i] + input[i + 1] + input[i + 2] < input[i + 1] + input[i + 2] + input[i + 3], the expression can be simplified to input[i] < input[i + 3].

# Implementing these, we can form a general solution as follows:

def count_increased_depths(input, sliding_window_size):
    count = 0
    for i in range(len(input) - sliding_window_size):
        if input[i] < input[i + sliding_window_size]:
            count += 1
    return count

print(count_increased_depths(input, 1))
print(count_increased_depths(input, 3))