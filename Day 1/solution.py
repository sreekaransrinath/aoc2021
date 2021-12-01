# Advent of Code 2021 Day 1 Solution
# Author: Sreekaran

import time

start = time.time()
with open((__file__.rstrip("solution.py") + "input.txt"), "r") as input_file:
    input = input_file.readlines()


def count(input, sliding_window_size):
    return len(
        [
            i
            for i in range(len(input) - sliding_window_size)
            if input[i] < input[i + sliding_window_size]
        ]
    )


print("Part One : ")
print(count(input, 1))

print("Part Two : ")
print(count(input, 3))

print("Time Taken: ", time.time() - start)
